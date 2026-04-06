# Hello World Agent

A simple Claude agent that creates a Hello World web page and opens it in a browser using Playwright MCP.

## What it does

1. Writes `hello.html` — a centered Hello World page with white background and large font
2. Starts a local HTTP server on port 8765
3. Opens the page via VS Code's Simple Browser

## Requirements

- Python 3.x
- Node.js + npx
- Claude Code CLI

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python hello_world_agent.py
```

Then open VS Code Simple Browser manually:
- `Ctrl+Shift+P` → `Simple Browser: Show` → `http://localhost:8765/hello.html`
