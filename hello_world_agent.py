import anyio
import sys
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

sys.stdout.reconfigure(encoding="utf-8")

async def main():
    async for message in query(
        prompt=(
            "Do the following steps in order:\n"
            "1. Write a file called hello.html in C:/Users/ecc_p/ with a Hello World page "
            "(white background, centered text, large font).\n"
            "2. Kill any process using port 8765, then start a Python HTTP server in the background "
            "with this exact command (do not wait for it): "
            "start /B python -m http.server 8765 --directory C:/Users/ecc_p/\n"
            "3. Wait 1 second, then open VS Code's Simple Browser by running: "
            "cmd /c start \"\" \"vscode://vscode.simpleBrowser/show?url=http://localhost:8765/hello.html\""
        ),
        options=ClaudeAgentOptions(
            allowed_tools=["Write", "Bash"],
            permission_mode="bypassPermissions",
        )
    ):
        if isinstance(message, ResultMessage):
            print("Done:", message.result)

anyio.run(main)
