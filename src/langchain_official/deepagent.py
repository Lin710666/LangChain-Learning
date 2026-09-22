# STEP1 Define the system prompt
## The system prompt defines your agent’s role and behavior. Keep it specific and actionable

SYSTEM_PROMPT = """You are a literary data assistant.

## Capabilities

- `fetch_text_from_url`: loads document text from a URL into the conversation.
Do not guess line counts or positions—ground them in tool results from the saved file."""

# STEP2 Create tools
## Tools let a model interact with external systems by calling functions you define
## Tools can depend on runtime context and also interact with agent memory.

import urllib.error
import urllib.request

from langchain.tools import tool

@tool
def fetch_text_from_url(url: str) -> str:
    """
    Fetch the document from a URL.
    """
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        return f"Fetch failed: {e}"
    text = raw.decode("utf-8", errors="replace")
    return text