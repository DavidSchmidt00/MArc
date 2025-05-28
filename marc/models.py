from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
from openai import OpenAI
import os

# LOCAL_ENDPOINT = "http://host.docker.internal:1234/v1"
# local_model_client = OpenAIChatCompletionClient(
#         base_url=LOCAL_ENDPOINT,
#         api_key="lm-studio",
#         model="gemma-3-4b-it-qat",
#         model_info=ModelInfo(
#             family="unkown",
#             function_calling=True,
#             json_output=False,
#             structured_output=True,
#             vision=False
#         )
#     )

if __name__ == "__main__":
    
    gemini_model = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY"),
    )
    for model in gemini_model.models.list():
        print(model)
    
gemini_model_client = OpenAIChatCompletionClient(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        model="gemini-2.0-flash",
        # model="gemini-2.5-flash-preview-05-20",
        api_key=os.getenv("GEMINI_API_KEY"),
        parallel_tool_calls=False,
        
        # max_tokens = 3500,
        # model_info=ModelInfo(
        #     family="unkown",
        #     function_calling=True,
        #     json_output=True,
        #     structured_output=True,
        #     vision=False
        # )
    )

# openai_client = OpenAIChatCompletionClient(
#   api_key=os.getenv("OPENAI_API_KEY")
# )

model_client=gemini_model_client
