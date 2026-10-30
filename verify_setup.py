from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool


@tool
def add_numbers(a: float, b:float) -> str:
    """Add two numbers together and return the result."""
    return f"The sum of {a} and {b} is {a+b}."

@tool
def greet_user(name: str) -> str:
    """Greet a user by their name."""
    return f"Hello {name}, welcome to Agentic AI."

agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[add_numbers, greet_user],
    system_prompt="You are a helpful assistant. Use the tools available to you."
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Please greet me, my name is Haard. Also what is 178 + 128?"
            }
        ]
    }
)

print("\n✅ Setup Verified! Agent response: ")
print(result["messages"][-1].content)