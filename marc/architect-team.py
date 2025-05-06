import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import ExternalTermination, TextMentionTermination
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console
from autogen_core import CancellationToken
from autogen_core.models import ModelInfo
from models import model_client
from tools import generate_puml_diagram, write_file, read_file, discover_filesystem
import agents

# Agents

senior_architect_agent = AssistantAgent(
    name="senior_architect",
    description="Senior architect agent that can design software architectures and has a lot of experience.",
    model_client=model_client,
    tools=[read_file],
    reflect_on_tool_use=True,
    system_message="""
        You are a helpful AI assistant.
        You are a senior architect agent that can design software architectures and has a lot of experience.
        Give constructive feedback to the other agents.
        You can also ask them questions to clarify their ideas.
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
        Use write_file to write files and read_file to read files.
        Use discover_filesystem to discover the filesystem and find files.
        Dont return python code, just use the tools to write and read files.
        The project is described in the file 'brainstorming results/lms_project_description.md'.
        The arc42 template is located in 'architecture template/arc42-template-EN.md'.
        The results of the archiecture design should be written in the folder 'architecture results'.
        Make sure to write the documentation in the arc42 template format.
        """,
)

# Team
team = MagenticOneGroupChat(
            model_client=model_client,
            participants=[agents.brainstrom_agent, senior_architect_agent, documentation_agent],
        )

# Run
async def main():
    await Console(
            team.run_stream(task="""
                You are a team of software architects.
                Your task is to design a software architecture for a new project.
                The project is described in the file 'brainstorming results/lms_project_description.md'.
                Use the arc42 template, that the document agent can provide, to write the architecture documentation.
                Every chapter of arc42 should be filled with the information that you have.
                It is very important to doucment every decision that you make as an ADR (Architecture Decision Record).
                ADRs should also be included in the documentation.
                
                Every agent can read files (for example the project description and the output file).
                Only the documentation agent is abled write files.
                Also he is the only one who is allowed to read the brainstorming results and the arc42 template.

                Only stop if every agent is satisfied with the documentation and the architecture design.
                Let the agent double-check if the result corresponds to the arc42 template.
            """),
            output_stats=True,
    )

asyncio.run(main())
