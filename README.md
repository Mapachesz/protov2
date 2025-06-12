# ProtoV2 Conversational Demo

This repository contains a small demo that performs a continuous conversation using
speech recognition (STT), text-to-speech (TTS) and a local language model via GPT4All.

## Requirements

- **Python** 3.10 or newer.
- The Python packages listed in `requirements.txt`.
- Vosk Spanish acoustic model.
- A GPT4All model, e.g. `mistral-7b-openorca.Q4_0.gguf`.

## Installation

1. Create a virtual environment with Python 3.10+ and activate it.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the Vosk model and place it under `models/vosk-es` so that the
   directory tree looks like:
   ```
   models/
     └── vosk-es/
         ├── am
         └── ...
   ```
   The Spanish model can be obtained from the [Vosk models page](https://alphacephei.com/vosk/models).

4. Download the GPT4All model `mistral-7b-openorca.Q4_0.gguf` from the
   [GPT4All release page](https://gpt4all.io/models/) and place it in the
   repository root or in the default GPT4All model directory.

## Usage

Run the main script to start the continuous conversation loop:

```bash
python main.py
```

Speak into your microphone and wait for the application to respond. To stop the
conversation press `Ctrl+C`.
