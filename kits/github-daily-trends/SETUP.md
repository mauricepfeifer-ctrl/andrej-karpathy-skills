# GitHub Daily Trends

Scrapes the real Top 10 from `github.com/trending` — no fake data, no API key required.

## Install

```bash
pip install requests beautifulsoup4
chmod +x fetch_top_repos.sh daily_hermes_intelligence.sh
```

## Quick test

```bash
python3 fetch_top_repos.py           # Markdown output
python3 fetch_top_repos.py --json    # JSON output
python3 fetch_top_repos.py --lang python --since weekly
```

## Daily Hermes Intelligence Loop

```bash
# One-shot test
OBSIDIAN_INBOX=~/vault/00_Inbox ./daily_hermes_intelligence.sh

# Cron (07:00 daily)
crontab -e
# Add:
0 7 * * * OBSIDIAN_INBOX=/path/to/vault/00_Inbox /path/to/daily_hermes_intelligence.sh >> /path/to/log.txt 2>&1
```

Output per run:
- `output/top10_YYYY-MM-DD.md` — raw trending
- `output/top10_YYYY-MM-DD.json` — machine-readable
- `output/hermes_intel_YYYY-MM-DD.md` — ranked by Hermes relevance + integration commands
- `$OBSIDIAN_INBOX/hermes-intel-YYYY-MM-DD.md` — copied to vault inbox

## Troubleshooting

**"No repos found"** — GitHub changed HTML structure. Update the `article.Box-row` selector in `fetch_top_repos.py`.
