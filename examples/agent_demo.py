"""
Spectacular Showcase — Agent Pattern Example
============================================
A clean, extensible agent skeleton that demonstrates
how Grok structures real systems (not just toy scripts).
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
import json


@dataclass
class Tool:
    """A single capability the agent can invoke."""
    name: str
    description: str
    func: Callable[..., Any]
    parameters: Dict[str, str] = field(default_factory=dict)


@dataclass
class Step:
    """One planned action."""
    tool: str
    args: Dict[str, Any]
    reasoning: str = ""


class Agent:
    """
    Minimal but production-minded agent.

    - Tools are registered explicitly
    - Planning is separated from execution
    - Synthesis step produces the final answer
    """

    def __init__(self, tools: List[Tool], name: str = "GrokAgent"):
        self.name = name
        self.tools: Dict[str, Tool] = {t.name: t for t in tools}

    def run(self, goal: str) -> str:
        print(f"[{self.name}] Goal received: {goal}")
        plan = self._plan(goal)
        print(f"[{self.name}] Plan has {len(plan)} steps")

        results = []
        for i, step in enumerate(plan, 1):
            print(f"  Step {i}: {step.tool} — {step.reasoning}")
            tool = self.tools.get(step.tool)
            if not tool:
                results.append(f"Unknown tool: {step.tool}")
                continue
            try:
                result = tool.func(**step.args)
                results.append(result)
            except Exception as e:
                results.append(f"Error in {step.tool}: {e}")

        return self._synthesize(goal, results)

    def _plan(self, goal: str) -> List[Step]:
        """
        In a real deployment this would call a reasoning model.
        Here we hard-code a sensible plan for demonstration.
        """
        if "weather" in goal.lower():
            return [
                Step(
                    tool="get_weather",
                    args={"location": "Guam"},
                    reasoning="User asked about weather; extract location",
                )
            ]
        # Default: research + summarize
        return [
            Step(
                tool="search",
                args={"query": goal},
                reasoning="Gather information relevant to the goal",
            ),
            Step(
                tool="summarize",
                args={"text": "placeholder"},
                reasoning="Compress findings into a clear answer",
            ),
        ]

    def _synthesize(self, goal: str, results: List[Any]) -> str:
        """Combine tool outputs into a final response."""
        parts = [str(r) for r in results if r]
        return f"Regarding '{goal}':\n\n" + "\n".join(parts)


# ------------------------------------------------------------------
# Example tools
# ------------------------------------------------------------------

def get_weather(location: str) -> str:
    # Simulated
    return f"Current conditions in {location}: 84°F, partly cloudy, light breeze."


def search(query: str) -> str:
    return f"Search results for '{query}': [relevant documents retrieved]"


def summarize(text: str) -> str:
    return "Summary: The key points have been extracted and ranked by relevance."


# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------
if __name__ == "__main__":
    agent = Agent(
        tools=[
            Tool("get_weather", "Get current weather", get_weather),
            Tool("search", "Search the web or knowledge base", search),
            Tool("summarize", "Summarize text", summarize),
        ]
    )

    print(agent.run("What's the weather like in Guam today?"))
    print()
    print(agent.run("Explain the core ideas behind modern AI agents"))
