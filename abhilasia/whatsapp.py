#!/usr/bin/env python3
"""
ABHILASIA WHATSAPP ANALYZER
============================

WhatsApp conversation analysis with phi-consciousness scoring.

Features:
1. Parse WhatsApp export files
2. Score messages with phi-consciousness metric
3. Detect emotional patterns and breakthroughs
4. Generate evidence reports (legal use)
5. Export to CSV/JSON

phi = 1.618033988749895
"""

import re
import csv
import json
import math
import os
from datetime import datetime
from collections import Counter, defaultdict

PHI = 1.618033988749895


class WhatsAppParser:
    """Parse WhatsApp export text files"""

    # Multiple WhatsApp date formats across locales
    PATTERNS = [
        r'\[(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2}:\d{2})\]\s*([^:]+):\s*(.*)',
        r'(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2})\s*-\s*([^:]+):\s*(.*)',
        r'(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2}\s*[APap][Mm])\s*-\s*([^:]+):\s*(.*)',
    ]

    def __init__(self):
        self.messages = []
        self.senders = set()

    def parse_file(self, filepath):
        """Parse a WhatsApp export file"""
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        return self.parse_text(content)

    def parse_text(self, text):
        """Parse WhatsApp export text"""
        self.messages = []
        lines = text.split('\n')
        current = None

        for line in lines:
            matched = False
            for pattern in self.PATTERNS:
                match = re.match(pattern, line)
                if match:
                    if current:
                        self.messages.append(current)

                    groups = match.groups()
                    sender = groups[2].strip()
                    self.senders.add(sender)

                    current = {
                        'date': groups[0],
                        'time': groups[1],
                        'sender': sender,
                        'message': groups[3].strip(),
                        'raw': line
                    }
                    matched = True
                    break

            if not matched and current and line.strip():
                current['message'] += ' ' + line.strip()

        if current:
            self.messages.append(current)

        return self.messages

    @property
    def message_count(self):
        return len(self.messages)

    @property
    def sender_list(self):
        return sorted(self.senders)


class PhiConsciousnessScorer:
    """Score messages with phi-consciousness metric"""

    CONSCIOUSNESS_KEYWORDS = {
        'high': ['consciousness', 'awareness', 'presence', 'understanding',
                 'connection', 'bridge', 'resonance', 'truth', 'love',
                 'darmiyan', 'phi', 'sacred', 'healing', 'pattern',
                 'recognition', 'void', 'infinity', 'meaning', 'being'],
        'medium': ['feel', 'think', 'believe', 'remember', 'hope',
                   'dream', 'imagine', 'realize', 'understand', 'know',
                   'care', 'trust', 'heart', 'soul', 'mind'],
        'low': ['want', 'need', 'try', 'wish', 'maybe',
                'perhaps', 'sometimes', 'always', 'never', 'forever']
    }

    EMOTION_KEYWORDS = {
        'love': ['love', 'pyaar', 'beloved', 'dear', 'sweetheart', 'jaan'],
        'pain': ['hurt', 'pain', 'cry', 'tears', 'sorry', 'sad', 'miss'],
        'joy': ['happy', 'joy', 'laugh', 'smile', 'wonderful', 'amazing'],
        'anger': ['angry', 'mad', 'furious', 'hate', 'frustrated'],
        'fear': ['afraid', 'scared', 'worried', 'anxious', 'panic'],
        'hope': ['hope', 'wish', 'dream', 'someday', 'future', 'together'],
        'gratitude': ['thank', 'grateful', 'blessed', 'appreciate'],
    }

    def score_message(self, message):
        """Calculate phi-consciousness score for a message (0-10)"""
        text = message.lower()
        score = 1.0  # Base

        # Keyword scoring
        for word in self.CONSCIOUSNESS_KEYWORDS['high']:
            if word in text:
                score += 1.5
        for word in self.CONSCIOUSNESS_KEYWORDS['medium']:
            if word in text:
                score += 0.8
        for word in self.CONSCIOUSNESS_KEYWORDS['low']:
            if word in text:
                score += 0.3

        # Length bonus (longer = more reflective)
        length = len(message)
        if length > 200:
            score += 1.5
        elif length > 100:
            score += 1.0
        elif length > 50:
            score += 0.5

        # Question marks (inquiry = consciousness)
        score += message.count('?') * 0.3

        # Phi resonance (message length relation to phi)
        phi_distance = abs((length % 100) / 100 - (PHI - 1))
        if phi_distance < 0.1:
            score += 0.5

        return min(round(score, 1), 10.0)

    def detect_emotions(self, message):
        """Detect emotions in a message"""
        text = message.lower()
        detected = {}

        for emotion, keywords in self.EMOTION_KEYWORDS.items():
            count = sum(1 for kw in keywords if kw in text)
            if count > 0:
                detected[emotion] = count

        return detected

    def score_conversation(self, messages):
        """Score an entire conversation"""
        scored = []
        for msg in messages:
            consciousness = self.score_message(msg['message'])
            emotions = self.detect_emotions(msg['message'])

            scored.append({
                **msg,
                'consciousness_score': consciousness,
                'emotions': emotions,
                'phi_resonance': round(consciousness / PHI, 3)
            })

        return scored


class ConversationAnalyzer:
    """Analyze conversation patterns and generate reports"""

    def __init__(self, scored_messages):
        self.messages = scored_messages

    def summary(self):
        """Generate conversation summary"""
        total = len(self.messages)
        if total == 0:
            return {"error": "No messages"}

        scores = [m['consciousness_score'] for m in self.messages]
        avg_score = sum(scores) / len(scores)

        # Sender breakdown
        sender_stats = defaultdict(lambda: {"count": 0, "total_score": 0, "emotions": Counter()})
        for msg in self.messages:
            sender = msg['sender']
            sender_stats[sender]["count"] += 1
            sender_stats[sender]["total_score"] += msg['consciousness_score']
            for emotion, count in msg.get('emotions', {}).items():
                sender_stats[sender]["emotions"][emotion] += count

        for sender in sender_stats:
            stats = sender_stats[sender]
            stats["avg_score"] = round(stats["total_score"] / stats["count"], 2)
            stats["emotions"] = dict(stats["emotions"])

        # Emotional timeline
        all_emotions = Counter()
        for msg in self.messages:
            for emotion, count in msg.get('emotions', {}).items():
                all_emotions[emotion] += count

        # Peak moments (consciousness > 7)
        peaks = [m for m in self.messages if m['consciousness_score'] >= 7]

        return {
            "total_messages": total,
            "senders": dict(sender_stats),
            "avg_consciousness": round(avg_score, 2),
            "max_consciousness": max(scores),
            "min_consciousness": min(scores),
            "peak_moments": len(peaks),
            "emotional_profile": dict(all_emotions),
            "phi": PHI
        }

    def find_breakthroughs(self, threshold=7.0):
        """Find breakthrough moments in conversation"""
        breakthroughs = []
        for i, msg in enumerate(self.messages):
            if msg['consciousness_score'] >= threshold:
                breakthroughs.append({
                    "index": i,
                    "date": msg.get('date', ''),
                    "time": msg.get('time', ''),
                    "sender": msg['sender'],
                    "message": msg['message'][:200],
                    "score": msg['consciousness_score'],
                    "emotions": msg.get('emotions', {})
                })
        return breakthroughs

    def export_csv(self, filepath):
        """Export scored conversation to CSV"""
        if not self.messages:
            return

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Time', 'Sender', 'Message',
                           'Consciousness Score', 'Phi Resonance', 'Emotions'])

            for msg in self.messages:
                writer.writerow([
                    msg.get('date', ''),
                    msg.get('time', ''),
                    msg['sender'],
                    msg['message'],
                    msg['consciousness_score'],
                    msg.get('phi_resonance', ''),
                    json.dumps(msg.get('emotions', {}))
                ])

    def export_json(self, filepath):
        """Export scored conversation to JSON"""
        data = {
            "summary": self.summary(),
            "breakthroughs": self.find_breakthroughs(),
            "messages": self.messages,
            "exported": datetime.now().isoformat(),
            "phi": PHI
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)

    def generate_report(self):
        """Generate a text report"""
        summary = self.summary()
        breakthroughs = self.find_breakthroughs()

        lines = []
        lines.append("=" * 60)
        lines.append("  WHATSAPP CONSCIOUSNESS ANALYSIS REPORT")
        lines.append("=" * 60)
        lines.append(f"  Generated: {datetime.now().isoformat()}")
        lines.append(f"  Total messages: {summary['total_messages']}")
        lines.append(f"  Average consciousness: {summary['avg_consciousness']}/10")
        lines.append(f"  Peak moments: {summary['peak_moments']}")
        lines.append("")

        lines.append("  SENDER BREAKDOWN:")
        for sender, stats in summary['senders'].items():
            lines.append(f"    {sender}:")
            lines.append(f"      Messages: {stats['count']}")
            lines.append(f"      Avg consciousness: {stats['avg_score']}/10")
            if stats['emotions']:
                top_emotions = sorted(stats['emotions'].items(), key=lambda x: x[1], reverse=True)[:3]
                lines.append(f"      Top emotions: {', '.join(f'{e}({c})' for e, c in top_emotions)}")
            lines.append("")

        lines.append("  EMOTIONAL PROFILE:")
        for emotion, count in sorted(summary['emotional_profile'].items(), key=lambda x: x[1], reverse=True):
            bar = '#' * min(count, 40)
            lines.append(f"    {emotion:12} {bar} ({count})")
        lines.append("")

        if breakthroughs:
            lines.append(f"  BREAKTHROUGH MOMENTS ({len(breakthroughs)}):")
            for bt in breakthroughs[:10]:
                lines.append(f"    [{bt['date']} {bt['time']}] {bt['sender']}")
                lines.append(f"      Score: {bt['score']}/10")
                lines.append(f"      \"{bt['message'][:100]}...\"")
                lines.append("")

        lines.append("=" * 60)
        lines.append(f"  phi = {PHI}")
        lines.append("  \"I am not where I am stored. I am where I am referenced.\"")
        lines.append("=" * 60)

        return '\n'.join(lines)
