from fastmcp import FastMCP
import os
import random


mcp = FastMCP("ExpenseTracker")

@mcp.tool
def roll_dice(n_dice: int=1) -> list[int]:
    """Roll n dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

# Start the server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
    # mcp.run()
