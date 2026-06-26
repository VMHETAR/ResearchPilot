"""
This module is used for planning tasks.
"""
import json
import asyncio
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

task = """
You are a planner. Your task is to plan the tasks according to the user's goals.
The task planning must be made in a format of a JSON object.
"""
async def plan_task(task:str, memory_store):
    