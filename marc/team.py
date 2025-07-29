from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.rate_limiters import InMemoryRateLimiter
from langgraph_supervisor import create_supervisor
import os

from marc import agents

def create_rate_limiter(requests_per_minute: int) -> InMemoryRateLimiter:
    """Creates a rate limiter for API requests.

    Args:
        requests_per_minute (int): The number of requests allowed per minute.

    Returns:
        InMemoryRateLimiter: An in-memory rate limiter instance.
    """
    return InMemoryRateLimiter(
        requests_per_second=requests_per_minute / 60,
        check_every_n_seconds=0.1,
        max_bucket_size=10,
    )

# --- LLM and API Key Configuration ---
# Load API keys from environment variables
GEMINI_API_KEY_FREE = os.getenv("GEMINI_API_KEY_1")
GEMINI_API_KEY_PAID = os.getenv("GEMINI_API_KEY_2")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize different language models with appropriate rate limiters
gemini_2_5_flash_free = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY_FREE, rate_limiter=create_rate_limiter(10))
gemini_2_5_flash_paid = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY_PAID, rate_limiter=create_rate_limiter(1000))
gemini_2_5_pro = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=GEMINI_API_KEY_PAID, rate_limiter=create_rate_limiter(150))
openai_o4_mini = ChatOpenAI(model="o4-mini", api_key=OPENAI_API_KEY, rate_limiter=create_rate_limiter(1000))
openai_o3 = ChatOpenAI(model="o3", api_key=OPENAI_API_KEY, rate_limiter=create_rate_limiter(500))

# Select the language model to be used by the agents
llm = openai_o3

# --- Agent Creation ---
# Create individual agents using the create_react_agent function from langgraph.
# Each agent is configured with a language model, name, tools, and a system prompt.
requirements_analyst_agent = create_react_agent(
    model=llm,
    name=agents.requirements_analyst_agent.name,
    tools=agents.requirements_analyst_agent.tools,
    prompt=agents.requirements_analyst_agent.system_prompt
)

architecture_design_agent = create_react_agent(
    model=llm,
    name=agents.architecture_design_agent.name,
    tools=agents.architecture_design_agent.tools,
    prompt=agents.architecture_design_agent.system_prompt
)

architecture_review_agent = create_react_agent(
    model=llm,
    name=agents.architecture_review_agent.name,
    tools=agents.architecture_review_agent.tools,
    prompt=agents.architecture_review_agent.system_prompt
)

adr_documentation_generation_agent = create_react_agent(
    model=llm,
    name=agents.adr_documentation_generation_agent.name,
    tools=agents.adr_documentation_generation_agent.tools,
    prompt=agents.adr_documentation_generation_agent.system_prompt
)

# --- Team and Supervisor Creation ---
# Create the supervisor agent that coordinates the team of agents.
# The supervisor is responsible for managing the workflow and communication between agents.
team = create_supervisor(
    model=llm,
    supervisor_name=agents.team_leader_agent.name,
    tools=agents.team_leader_agent.tools,
    prompt=agents.team_leader_agent.system_prompt,
    agents=[architecture_design_agent, architecture_review_agent, adr_documentation_generation_agent, requirements_analyst_agent],
    add_handoff_back_messages=True,
    add_handoff_messages=True,
).compile()
