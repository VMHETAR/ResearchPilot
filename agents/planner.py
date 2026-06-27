"""
Planner Agent
Generates an execution plan for a user's research goal.
"""

import json
from pathlib import Path

from models.llm import BaseLLM

SYSTEM_PROMPT = Path(
    "prompts/planner.md"
).read_text(encoding="utf-8")


async def plan_task(
    user_goal: str,
    llm: BaseLLM,
    memory_store=None,
) -> dict | None:

    response = await llm.generate(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_goal,
    )

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        return None