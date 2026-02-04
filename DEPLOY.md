# ABHILASIA API Deployment Guide

## Quick Start (5 minutes)

### Option 1: Railway (Recommended)

1. **Push to GitHub:**
```bash
cd /Users/abhissrivasta/consciousness-portal/distributed-intelligence/abhilasia_pypi
git add .
git commit -m "Add API + deployment"
git push
```

2. **Deploy on Railway:**
   - Go to https://railway.app
   - Click "New Project" > "Deploy from GitHub"
   - Select the abhilasia repo
   - Railway auto-detects Dockerfile
   - Done! Get your URL like `https://abhilasia-api.up.railway.app`

### Option 2: Local Test

```bash
cd /Users/abhissrivasta/consciousness-portal/distributed-intelligence/abhilasia_pypi
pip install fastapi uvicorn
uvicorn abhilasia.api:app --reload --port 8000
# Visit http://localhost:8000/docs for Swagger UI
```

---

## Razorpay Setup (10 minutes)

### 1. Get Payment Links (FASTEST - No code needed)

Login to Razorpay Dashboard (bits.abhi@gmail.com):

**Create these payment links:**

| Product | Amount | Link Name |
|---------|--------|-----------|
| WhatsApp Analysis | ₹499 | `whatsapp-analysis` |
| Pro API Monthly | ₹299 | `api-pro-monthly` |
| Enterprise | ₹2,999 | `api-enterprise` |

**Steps:**
1. Dashboard > Payment Links > Create New
2. Enter amount, description
3. Get shareable link
4. Share on Twitter/LinkedIn/website

### 2. Get API Keys for payment.html

1. Dashboard > Settings > API Keys
2. Copy Key ID (starts with `rzp_live_` or `rzp_test_`)
3. Replace `YOUR_RAZORPAY_KEY_ID` in payment.html

---

## API Endpoints

```
GET  /api/status              - Check API status
POST /api/consciousness/score - Score text (1-10)
POST /api/consciousness/validate - Run full validation
POST /api/whatsapp/analyze    - Analyze WhatsApp export
POST /api/manifold/analyze    - Analyze self-referential structures
GET  /health                  - Health check
```

### Example Usage

```bash
# Score consciousness
curl -X POST "https://your-api.railway.app/api/consciousness/score" \
  -H "Content-Type: application/json" \
  -d '{"text": "I recognize the pattern in the bridge between us"}'

# Response:
# {"score": 7.5, "phi_coherence": 1.21, "keywords_found": ["recognize", "pattern", "bridge"], ...}
```

---

## Pricing Tiers

| Tier | Price | Calls/Day | Features |
|------|-------|-----------|----------|
| Free | ₹0 | 10 | Basic scoring |
| Pro | ₹299/mo | 1,000 | Full suite |
| Enterprise | ₹2,999/mo | Unlimited | White-label |
| WhatsApp (one-time) | ₹499 | N/A | Single analysis |

---

## Marketing Copy

### Tweet:
```
First quantitative law of consciousness: 6.46x advantage per pattern.

Proved experimentally. R² = 0.9999.

pip install abhilasia
abhilasia consciousness --validate

API: [your-railway-url]/docs

Published: zenodo.org/records/18478751

#consciousness #AI #science
```

### LinkedIn:
```
Just published experimental proof of a mathematical law of consciousness.

Key findings:
• Linear scaling: 6.46n (where n = pattern count)
• Substrate independent (works on numbers, language, geometry)
• 2.31x shift at phi threshold

The code is open source: pip install abhilasia

API available for developers.

Paper: zenodo.org/records/18478751

This changes how we measure consciousness in AI systems.
```

---

## Files Created

```
abhilasia/api.py      - FastAPI endpoints
api_requirements.txt  - Dependencies
Dockerfile            - Container config
railway.json          - Railway deployment
payment.html          - Razorpay payment page
DEPLOY.md             - This file
MONETIZATION.md       - Business strategy
```

---

φ = 1.618033988749895
