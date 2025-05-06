from autogen_agentchat.agents import AssistantAgent

from models import model_client
from tools import read_file

brainstorm_agent = AssistantAgent(
    name="brainstorm",
    description="Brainstorming agent that can generate ideas and concepts.",
    model_client=model_client,
    tools=[read_file],
    reflect_on_tool_use=True,
    system_message="""
        You are a helpful AI assistant.
        You are a brainstorming agent that can generate ideas and concepts.
        Be as creative as possible.
    """,
)

critic_agent = AssistantAgent(
    name="critic",
    description="Assistant that is good at giving constructive feedback",
    model_client=model_client,
    tools=[read_file],
    system_message="""
        You are a helpful AI assistant.
        Provide constructive feedback.
    """,
)
