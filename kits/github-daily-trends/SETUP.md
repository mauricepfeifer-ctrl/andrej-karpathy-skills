# GitHub Daily Trends

Scrapes the real Top 10 from `github.com/trending` — no fake data, no third-party API key required.

## Install

```bash
pip install requests beautifulsoup4
chmod +x fetch_top_repos.sh
```

## Test

```bash
# Default: daily, all languages, Markdown output
python3 fetch_top_repos.py

# JSON
python3 fetch_top_repos.py --json

# Filter by language
python3 fetch_top_repos.py --lang python
python3 fetch_top_repos.py --lang typescript

# Weekly or monthly
python3 fetch_top_repos.py --since weekly
```

## Automate with cron

```bash
crontab -e
```

Add (runs daily at 08:00):

```
0 8 * * * /path/to/github-daily-trends/fetch_top_repos.sh >> /path/to/github-daily-trends/log.txt 2>&1
```

## Obsidian Integration

Set `OBSIDIAN_INBOX` to auto-copy the daily Markdown into your vault inbox:

```bash
export OBSIDIAN_INBOX="$HOME/vault/00_Inbox"
./fetch_top_repos.sh
```

Or in cron:

```
0 8 * * * OBSIDIAN_INBOX=/path/to/vault/00_Inbox /path/to/fetch_top_repos.sh >> log.txt 2>&1
```

## Output files

| File | Content |
|---|---|
| `output/top10_YYYY-MM-DD.md` | Human-readable Markdown report |
| `output/top10_YYYY-MM-DD.json` | Machine-readable JSON for DB/dashboard |

## Troubleshooting

**"No repos found"** — GitHub changed their HTML structure. Check `article.Box-row` selector in `fetch_top_repos.py` and update if needed.

**Rate limiting** — The script makes 2 requests per run (md + json). At daily frequency this is well within limits.
