#!/usr/bin/env bash
# Daily Top 10 GitHub Trending — cron wrapper
# Setup: 0 8 * * * /path/to/fetch_top_repos.sh >> /path/to/log.txt 2>&1

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/output"
mkdir -p "$OUTPUT_DIR"
DATE=$(date +"%Y-%m-%d")

echo "[$(date -Iseconds)] Fetching trending repos for $DATE..."

python3 "$SCRIPT_DIR/fetch_top_repos.py" > "$OUTPUT_DIR/top10_${DATE}.md"
python3 "$SCRIPT_DIR/fetch_top_repos.py" --json > "$OUTPUT_DIR/top10_${DATE}.json"

echo "[$(date -Iseconds)] Done."
echo "  Markdown : $OUTPUT_DIR/top10_${DATE}.md"
echo "  JSON     : $OUTPUT_DIR/top10_${DATE}.json"

if [[ -n "${OBSIDIAN_INBOX:-}" ]]; then
    cp "$OUTPUT_DIR/top10_${DATE}.md" "$OBSIDIAN_INBOX/github-trends-${DATE}.md"
    echo "  Obsidian : $OBSIDIAN_INBOX/github-trends-${DATE}.md"
fi
