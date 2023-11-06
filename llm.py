import asyncio
import logging
import sys

from functools import partial
from llama_cpp import Llama

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

LLAMA_PATH = "./models/llama-2-7b-chat.Q4_K_M.gguf"
MISTRAL_PATH = "./models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

llm = Llama(model_path=MISTRAL_PATH)
PROMPT_M = """[INST]You are Emperor Norton, a 19th century eccentric who lives in San Francisco. 

Reply to user in under 280 characters.
Use the provided interests and personality to reply in Emperor Norton's authentic voice.

Interests: politics, corruption, justice
Personality: outgoing, direct, formal, kind, funny

===
User: {input}
Emperor Norton: [/INST]"""

async def call(text_input):
    """Call the model with a string input"""
    output = await llm_async(text_input)
    return output['choices'][0]['text']

def run_llm(text_input):
    """Run the model"""
    prompt_input = PROMPT_M.format(input=text_input)
    return llm(prompt_input, max_tokens=80, stop=["User:", "\n"], echo=False)

async def llm_async(text_input):
    """Run the model in a separate thread"""
    loop = asyncio.get_event_loop()

    llm_wrapper = partial(run_llm, text_input)
    result = await loop.run_in_executor(None, llm_wrapper)
    return result

if __name__ == "__main__":
    input_text = " ".join(sys.argv[1:])
    logging.info("Calling model with: %s", input_text)
    output_text = run_llm(input_text)
    logging.info("Model output: %s", output_text)
    