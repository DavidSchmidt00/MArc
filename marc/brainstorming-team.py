import asyncio
from typing import Literal

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_core.models import ModelInfo
from autogen_ext.models.openai import OpenAIChatCompletionClient
from models import model_client
from tools import generate_puml_diagram, write_file, read_file, discover_filesystem
import agents

# Agents


architect_agent = AssistantAgent(
    name="senior_architect",
    description="Senior software architect with a lot of experience.",
    model_client=model_client,
    tools=[read_file],
    system_message="""
        You are a helpful AI assistant.
        You are a Senior software architect with a lot of experience.
    """,
)

documentation_agent = AssistantAgent(
    name="documentation",
    description="Documentation agent that can write documentation into files and read files.",
    tools=[write_file, read_file, discover_filesystem],
    model_client=model_client,
    reflect_on_tool_use=True,
    system_message="""
        You are a documentation agent that can write documentation into files and read files.
        Use write_file to write files and read_file to read files, use discover_filesystem to discover the filesystem and find files.
        If the reading or writing returns an error, use discover_filesystem to find an appropriate place.
        If you cant find a file, just return an error message, dont return python code as you cannot execute code!
        Please use easy to read formats like markdown or asciidoc.
        """,
)


# Team
team = MagenticOneGroupChat(
            model_client=model_client, 
            participants=[agents.brainstorm_agent, agents.critic_agent, documentation_agent, architect_agent],
        )

# Run
async def main():
    await Console(
            team.run_stream(task="""
                I want to challange a llm-based multi-agent-system that should simulate a whole architecture team.
                Generate a comprehensive description of a softwarearchitecture-project that can be used for that.
                The result should include the following information:
                * context
                * description of the project
                * requirements to the system in the form of user-stories
                * key stakeholder
                * quality attributes
                If you find additional information that is important for the project, include it as well.
                
                Every agent can read files (for example the result) but only the documentation agent can write files.

                The result shoud be written into a file and be in a format that is easy to read and understand.
                Only stop if all agents agree that the task is done.
            """),
            output_stats=True,
    )

asyncio.run(main())
