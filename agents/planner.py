"""
This module is used for planning tasks.
"""
import json
import asyncio
from mcp.server.fastmcp import FastMCP
import os
from pathlib import Path

mcp = FastMCP()

SYSTEM_PROMPT = Path("prompts/planner.md").read_text()
async def plan_task(task:str, llm, memory_store=None,) -> dict|None:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": task},
    ]