#!/usr/bin/env python3
"""
Fetch top 10 GitHub trending repos.
Usage: python3 fetch_top_repos.py [--json] [--lang python] [--since daily|weekly|monthly]
Requires: pip install requests beautifulsoup4
"""
import argparse
import json
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def fetch_trending(lang: str = "", since: str = "daily") -> list[dict]:
    url = f"https://github.com/trending/{lang}" if lang else "https://github.com/trending"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    resp = requests.get(url, params={"since": since}, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    repos = []

    for article in soup.select("article.Box-row")[:10]:
        link = article.select_one("h2 a, h1 a")
        if not link:
            continue
        full_name = link.get("href", "").strip("/")
        if not full_name or "/" not in full_name:
            continue

        desc_el = article.select_one("p")
        desc = desc_el.get_text(strip=True) if desc_el else ""

        lang_el = article.select_one('[itemprop="programmingLanguage"]')
        language = lang_el.get_text(strip=True) if lang_el else ""

        stars_today = 0
        for span in article.find_all("span"):
            text = span.get_text(strip=True)
            if "stars today" in text or "star today" in text:
                digits = "".join(c for c in text.split("star")[0] if c.isdigit())
                stars_today = int(digits) if digits else 0
                break

        total_stars = 0
        for a in article.select("a"):
            if str(a.get("href", "")).endswith("/stargazers"):
                digits = "".join(c for c in a.get_text() if c.isdigit())
                total_stars = int(digits) if digits else 0
                break

        repos.append({
            "name": full_name,
            "url": f"https://github.com/{full_name}",
            "desc": desc,
            "lang": language,
            "stars_today": stars_today,
            "total_stars": total_stars,
        })

    return repos


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch top 10 GitHub trending repos")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--lang", default="", help="Language filter, e.g. python")
    parser.add_argument("--since", default="daily", choices=["daily", "weekly", "monthly"])
    args = parser.parse_args()

    repos = fetch_trending(lang=args.lang, since=args.since)
    if not repos:
        print("No repos found — GitHub trending page structure may have changed.", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps({
            "date": datetime.now().isoformat(),
            "since": args.since,
            "lang_filter": args.lang or "all",
            "top10": repos,
        }, indent=2, ensure_ascii=False))
        return

    date_str = datetime.now().strftime("%Y-%m-%d")
    lang_label = f" ({args.lang})" if args.lang else ""
    print(f"# Top 10 GitHub Trending{lang_label} — {date_str} ({args.since})\n")
    for i, repo in enumerate(repos, 1):
        lang_tag = f"**{repo['lang']}** · " if repo["lang"] else ""
        print(f"## {i}. [{repo['name']}]({repo['url']})")
        print(f"{lang_tag}+{repo['stars_today']:,} stars today · {repo['total_stars']:,} total")
        if repo["desc"]:
            print(repo["desc"])
        print()


if __name__ == "__main__":
    main()
