#!/usr/bin/env bash
# Daily Hermes Intelligence Loop
# fetch -> score -> Obsidian inbox
#
# Cron (07:00 daily):
#   0 7 * * * OBSIDIAN_INBOX=/path/to/vault/00_Inbox /path/to/daily_hermes_intelligence.sh >> log.txt 2>&1

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/output"
mkdir -p "$OUTPUT_DIR"
DATE=$(date +"%Y-%m-%d")

echo "[$(date -Iseconds)] === Hermes Daily Intelligence: $DATE ==="

python3 "$SCRIPT_DIR/fetch_top_repos.py" --json > "$OUTPUT_DIR/top10_${DATE}.json"
python3 "$SCRIPT_DIR/fetch_top_repos.py"        > "$OUTPUT_DIR/top10_${DATE}.md"

python3 "$SCRIPT_DIR/score_repos.py" \
    < "$OUTPUT_DIR/top10_${DATE}.json" \
    > "$OUTPUT_DIR/hermes_intel_${DATE}.md"

echo "  Raw     : $OUTPUT_DIR/top10_${DATE}.md"
echo "  Intel   : $OUTPUT_DIR/hermes_intel_${DATE}.md"

if [[ -n "${OBSIDIAN_INBOX:-}" ]]; then
    cp "$OUTPUT_DIR/hermes_intel_${DATE}.md" "$OBSIDIAN_INBOX/hermes-intel-${DATE}.md"
    echo "  Obsidian: $OBSIDIAN_INBOX/hermes-intel-${DATE}.md"
fi

echo "[$(date -Iseconds)] === Done ==="
