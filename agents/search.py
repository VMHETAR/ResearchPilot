""" 
Search Agent
Searches for relevant scientific papers based on a user's research goal.
"""
import json
import urllib, urllib.parse
from pathlib import Path
from models.llm import BaseLLM
from mcp.server.fastmcp import FastMCP
SYSTEM_PROMPT = Path("prompts/search.md").read_text(encoding="utf-8")

"""
This function searches papers through multiple sources.

"""

mcp = FastMCP("Research Search")

@mcp.tool()
async def search_research_papers(query:str) -> dict[str, dict]|None:
    """
    Search for relevant scientific papers based on a user's research goals.
    """
    