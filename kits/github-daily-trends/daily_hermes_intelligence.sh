#!/usr/bin/env bash
# Daily Hermes Intelligence Loop
# fetch GitHub trending -> score for Hermes relevance -> drop into Obsidian inbox
#
# Cron (07:00 daily):
#   0 7 * * * OBSIDIAN_INBOX=/path/to/vault/00_Inbox /path/to/daily_hermes_intelligence.sh >> /path/to/log.txt 2>&1

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/output"
mkdir -p "$OUTPUT_DIR"
DATE=$(date +"%Y-%m-%d")

echo "[$(date -Iseconds)] === Hermes Daily Intelligence: $DATE ==="

# 1. Fetch real trending data
echo "[$(date -Iseconds)] Fetching GitHub trending..."
python3 "$SCRIPT_DIR/fetch_top_repos.py" --json > "$OUTPUT_DIR/top10_${DATE}.json"
python3 "$SCRIPT_DIR/fetch_top_repos.py"        > "$OUTPUT_DIR/top10_${DATE}.md"

# 2. Score for Hermes relevance
echo "[$(date -Iseconds)] Scoring repos..."
python3 "$SCRIPT_DIR/score_repos.py" \
    < "$OUTPUT_DIR/top10_${DATE}.json" \
    > "$OUTPUT_DIR/hermes_intel_${DATE}.md"

echo "[$(date -Iseconds)] Output:"
echo "  Raw trending : $OUTPUT_DIR/top10_${DATE}.md"
echo "  Hermes intel : $OUTPUT_DIR/hermes_intel_${DATE}.md"

# 3. Drop into Obsidian inbox (if configured)
if [[ -n "${OBSIDIAN_INBOX:-}" ]]; then
    cp "$OUTPUT_DIR/hermes_intel_${DATE}.md" "$OBSIDIAN_INBOX/hermes-intel-${DATE}.md"
    echo "  Obsidian     : $OBSIDIAN_INBOX/hermes-intel-${DATE}.md"
fi

# 4. Optional: push top pick into Hermes inbox via CLI
# TOP_NAME=$(python3 -c "
import json
d=json.load(open('$OUTPUT_DIR/top10_${DATE}.json'))
print(d['top10'][0]['name'])
# ")
# hermes inbox add "GitHub Intel $DATE: $TOP_NAME" 2>/dev/null || true

echo "[$(date -Iseconds)] === Done ==="
