"""
Obsidian connector via obsidian-local-rest-api.
Requires: pip install requests
Config:   OBSIDIAN_API_KEY  env var (required)
          OBSIDIAN_PORT     env var (default: 27124)
          OBSIDIAN_SCHEME   env var (default: https)
          OBSIDIAN_SSL_VERIFY env var (default: false — self-signed cert)
"""
import os
import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

_SCHEME = os.getenv("OBSIDIAN_SCHEME", "https")
_BASE = f"{_SCHEME}://localhost:{os.getenv('OBSIDIAN_PORT', '27124')}"
_HEADERS = {
    "Authorization": f"Bearer {os.getenv('OBSIDIAN_API_KEY', '')}",
}
_VERIFY = os.getenv("OBSIDIAN_SSL_VERIFY", "false").lower() == "true"


def _get(path: str, params: dict | None = None) -> requests.Response:
    return requests.get(
        f"{_BASE}/{path.lstrip('/')}",
        headers=_HEADERS,
        params=params,
        verify=_VERIFY,
        timeout=10,
    )


def _put(path: str, content: str) -> requests.Response:
    h = {**_HEADERS, "Content-Type": "text/markdown"}
    return requests.put(
        f"{_BASE}/{path.lstrip('/')}",
        headers=h,
        data=content.encode("utf-8"),
        verify=_VERIFY,
        timeout=10,
    )


def search(query: str) -> list[dict]:
    """Search vault. Returns list of {filename, score, matches}."""
    resp = _get("search/simple/", params={"query": query, "contextLength": 100})
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
