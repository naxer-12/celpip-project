#!/usr/bin/env bash
# Ping Render service to keep the free-tier container active and prevent spin-downs
RENDER_URL="https://celpip-project.onrender.com"

# Check /healthz first; fall back to root / if /healthz is not yet deployed
STATUS=$(curl -s -o /dev/null -w "%{http_code}" -m 25 "${RENDER_URL}/healthz" 2>/dev/null)
if [ "$STATUS" != "200" ]; then
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" -m 25 "${RENDER_URL}/" 2>/dev/null)
fi

if [ "$STATUS" = "200" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Render service is active (HTTP $STATUS)"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Ping completed with status: HTTP $STATUS"
fi
