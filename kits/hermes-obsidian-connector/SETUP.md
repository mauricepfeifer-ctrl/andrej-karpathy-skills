# Hermes Obsidian Connector

Minimal Python connector between Hermes agents and your Obsidian vault via [obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api).

## Prerequisites

1. Obsidian running with the **Local REST API** community plugin enabled
2. Plugin settings → copy your API key
3. Default port: `27124`

## Install

```bash
pip install requests
cp connector.py /path/to/your/project/
```

## Config

```bash
export OBSIDIAN_API_KEY="your-key-here"
# optional:
export OBSIDIAN_PORT="27124"
```

## Usage

```python
from connector import search, read, write_to_inbox

# Search across vault
results = search("Rechtsstreit")
for r in results:
    print(r["filename"], r["score"])

# Read a specific note
content = read("02_Intelligence/karpathy-wiki.md")

# Drop a note into inbox (Hermes capture)
path = write_to_inbox("hermes-capture-2026-06-28", "# Today's capture\n\n...")
print(f"Written to {path}")
```

## API

| Function | Args | Returns |
|---|---|---|
| `search(query)` | query string | `list[{filename, score, matches}]` |
| `read(vault_path)` | path relative to vault root | note content as string |
| `write_to_inbox(title, content)` | title (no .md), markdown content | vault path written |

## Integration with Hermes

Drop `connector.py` next to your Hermes agent. Import as needed:

```python
from connector import search, write_to_inbox

def handle_obsidian_capture(payload):
    write_to_inbox(payload["title"], payload["content"])
```

## Vault path convention

This connector assumes your inbox folder is `00_Inbox/`. Adjust the path in `write_to_inbox()` if your vault uses a different structure.
