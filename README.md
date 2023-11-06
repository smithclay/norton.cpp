## norton.cpp

Lightweight Emperor Norton on Discord

### requirements

* python3
* model(s) (GGUF) from https://huggingface.co/TheBloke saved to `models/`

### running

* Download a GGUF model for HuggingFace to the `models/` directory, prompt is currently tested with [Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/blob/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf)
* Install requirements: `pip3 install -r requirements.txt`
* Talk to Emperor Norton: `python3 llm.py Greetings Emperor!` 

_or_

* Run the Discord bot powered by Emperor Norton `DISCORD_BOT_TOKEN=... python3 bot.py`
