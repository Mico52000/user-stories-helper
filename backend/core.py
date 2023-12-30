import os

from dotenv import load_dotenv
from langchain.llms import LlamaCpp
from langchain.llms import GPT4All
from langchain.chains import ConversationChain

import typing

from langchain.memory import ConversationBufferWindowMemory, ConversationSummaryBufferMemory

load_dotenv()

model_path = os.getenv("MODELS_PATH")
llm_path = os.path.join(model_path, "mixtral-8x7b-v0.1.Q3_K_M.gguf")
n_gpu_layers = 1  # Change this value based on your model and your GPU VRAM pool.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
llm = LlamaCpp(
    model_path=llm_path,
    temperature=0,
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    max_tokens=20000,
    n_ctx=4096,
    max_new_tokens=1000,

    verbose=True,  # Verbose is required to pass to the callback manager
)
memory=ConversationSummaryBufferMemory(
        llm=llm,
        max_token_limit=400
)
#memory=ConversationBufferWindowMemory(k=3)
conversation = ConversationChain(
    llm=llm,
    memory=memory
)
def run_llm(query: str) -> any:




    return conversation({"input":query},)


if __name__ == "__main__":
    print(run_llm("what are the type of chains in langchain"))