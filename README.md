# Hello World Agent

A simple Claude agent that creates a Hello World web page and serves it locally.

## What it does

1. Writes `hello.html` — a centered Hello World page with white background and large font
2. Starts a local HTTP server on port 8765
3. Prints the URL: `http://localhost:8765/hello.html`

## Requirements

- Python 3.x
- Claude Code CLI

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python hello_world_agent.py
```

Open `http://localhost:8765/hello.html` in any browser.
