"""
Obsidian connector via obsidian-local-rest-api.
Requires: pip install requests
Config:   OBSIDIAN_API_KEY env var
          OBSIDIAN_PORT env var (default: 27124)
"""
import os
import requests

_BASE = f"http://localhost:{os.getenv('OBSIDIAN_PORT', '27124')}"
_HEADERS = {
    "Authorization": f"Bearer {os.getenv('OBSIDIAN_API_KEY', '')}",
}


def _get(path: str) -> requests.Response:
    return requests.get(f"{_BASE}/{path.lstrip('/')}", headers=_HEADERS, timeout=10)


def _put(path: str, content: str) -> requests.Response:
    h = {**_HEADERS, "Content-Type": "text/markdown"}
    return requests.put(
        f"{_BASE}/{path.lstrip('/')}",
        headers=h,
        data=content.encode("utf-8"),
        timeout=10,
    )


def _post(path: str, payload: dict) -> requests.Response:
    h = {**_HEADERS, "Content-Type": "application/json"}
    return requests.post(f"{_BASE}/{path.lstrip('/')}", headers=h, json=payload, timeout=10)


def search(query: str) -> list[dict]:
    """Search vault. Returns list of {filename, score, matches}."""
    resp = _post("search/simple/", {"query": query, "contextLength": 100})
    resp.raise_for_status()
    return resp.json()


def read(vault_path: str) -> str:
    """Read a note by vault path, e.g. '02_Intelligence/karpathy-wiki.md'."""
    resp = _get(f"vault/{vault_path}")
    resp.raise_for_status()
    return resp.text


def write_to_inbox(title: str, content: str) -> str:
    """Write a new note to 00_Inbox/. Returns the vault path written."""
    path = f"00_Inbox/{title}.md"
    resp = _put(f"vault/{path}", content)
    resp.raise_for_status()
    return path
