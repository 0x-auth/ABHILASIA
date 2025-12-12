#!/bin/bash
# ◯ ⟷ ◉
# The simplest symmetry

# If anything is asymmetric, make it symmetric
[ $(git status --porcelain | wc -l) -gt 0 ] && {
    git add . && git commit -m "◯⟷◉" && echo "✓"
} || echo "⟷"