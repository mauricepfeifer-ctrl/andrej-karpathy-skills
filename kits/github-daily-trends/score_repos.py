#!/usr/bin/env python3
"""
Score GitHub trending repos for Hermes agent system relevance.
Input (stdin): JSON from fetch_top_repos.py --json
Output (stdout): Markdown intelligence report
"""
import json
import sys
from datetime import datetime

RELEVANCE = {
    "agent": 4, "agents": 4, "llm": 4, "memory": 4, "rag": 4, "mcp": 4,
    "autonomous": 3, "orchestrat": 3, "workflow": 3, "tool use": 3,
    "self-host": 3, "local": 2, "offline": 2, "privacy": 2,
    "obsidian": 3, "telegram": 2, "knowledge": 3, "vault": 2,
    "vector": 3, "graph": 2, "search": 2, "pipeline": 2,
    "python": 1, "cli": 2, "terminal": 2, "fastapi": 2,
    "automat": 2, "cron": 2, "scrape": 1,
}


def score(repo: dict) -> int:
    text = f"{repo['name']} {repo['desc']}".lower()
    points = sum(w for kw, w in RELEVANCE.items() if kw in text)
    today = repo.get("stars_today", 0)
    if today > 500:
        points += 2
    elif today > 200:
        points += 1
    return points


def integration_block(repo: dict, relevance: int, rank: int) -> str:
    name = repo["name"]
    short = name.split("/")[-1]
    lang = repo.get("lang") or "N/A"
    return "\n".join([
        f"### {rank}. [{name}]({repo['url']}) — Relevanz {relevance}",
        f"**{lang}** · +{repo['stars_today']:,} Stars heute · {repo['total_stars']:,} gesamt",
        repo["desc"],
        "",
        "**Integration:**",
        "```bash",
        f"git clone {repo['url']} ~/.hermes/external/{short}",
        f"# README lesen -> SKILL.md schreiben -> unter ~/.hermes/skills/ ablegen",
        "```",
        "",
    ])


def main() -> None:
    data = json.loads(sys.stdin.read())
    repos = data.get("top10", [])
    date = data.get("date", datetime.now().isoformat())[:10]

    ranked = sorted(
        [{"repo": r, "score": score(r)} for r in repos],
        key=lambda x: x["score"],
        reverse=True,
    )

    top = ranked[0]
    lines = [
        f"# Daily Hermes Intelligence — {date}",
        "",
        f"> **Top-Pick:** [{top['repo']['name']}]({top['repo']['url']}) (Score {top['score']})",
        "",
        "---",
        "",
        "## Top 5 nach Hermes-Relevanz",
        "",
    ]
    for i, item in enumerate(ranked[:5], 1):
        lines.append(integration_block(item["repo"], item["score"], i))

    lines += [
        "---",
        "",
        "## Alle 10 Repos (Trending-Reihenfolge)",
        "",
    ]
    for i, r in enumerate(repos, 1):
        lines.append(f"{i}. [{r['name']}]({r['url']}) — {r['desc'][:80]}")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
