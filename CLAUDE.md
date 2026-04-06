# Hello World Agent

A Claude agent that creates a Hello World web page and serves it locally.

## Project Structure

- `hello_world_agent.py` — main agent script
- `hello.html` — generated Hello World page
- `requirements.txt` — Python dependencies

## Setup

```bash
pip install -r requirements.txt
```

## Running the Agent

```bash
python hello_world_agent.py
```

The agent will:
1. Write `hello.html` to this folder
2. Start an HTTP server on port 8765
3. Print the URL: http://localhost:8765/hello.html

Open the URL in any browser to view the page.

## Notes

- Files are served from `C:/Users/ecc_p/Dev/hello_world_agent/`
- If port 8765 is already in use, the agent will kill the existing process first
