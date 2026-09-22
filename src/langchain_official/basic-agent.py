from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

## LangChain 会把你传进去的普通函数转成 StructuredTool，
## 工具的「描述」默认取自函数的 docstring
def get_weather(city: str) -> str:
    '''Gat weather for a given city.'''
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="deepseek-flash",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)