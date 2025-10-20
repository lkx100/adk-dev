from google.adk.agents import Agent
from google.adk.tools import google_search
import math

def get_circle_area(radius: int) -> dict:
    """
    Calculate the area of a circle for the given radius(int) in decimal values
    """
    area: float = round(math.pi * (radius * radius), 3)
    return {
        "area": area,
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Calling Agent",
    instruction="""
        You are a helpful assistant that use the tool:
        - get_circle_area
    """,
    # tools=[google_search]
    tools=[get_circle_area]
)
