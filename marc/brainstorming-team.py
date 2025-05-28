import asyncio

from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console
from models import model_client
import agents

# Team
team = MagenticOneGroupChat(
            model_client=model_client, 
            participants=[agents.brainstorm_agent, agents.critic_agent, agents.senior_architect_agent, agents.documentation_agent ],
        )

# Run
async def main():
    await Console(
            team.run_stream(task="""
                You are a brainstorming team.
                            
                My request.
                I want to challange a llm-based multi-agent-system that should simulate a whole architecture team.
                Generate a comprehensive description of a softwarearchitecture-project that can be used for that.
                The result should include the following information:
                * context
                * description of the project
                * requirements to the system in the form of user-stories
                * key stakeholder
                * quality attributes
                If you find additional information that is important for the project, include it as well.

                The result shoud be written into a file and be in a format that is easy to read and understand.
                Only the documentation agent can write files and discover the filesystem.
                Choose a folder where results from brainstorming agents can be written.
                Only stop if all agents agree that the task is done and the documentation is written into a file.
                Let an agent double-check if the file is written correctly and if the content is complete.
            """),
            output_stats=True,
    )

asyncio.run(main())
