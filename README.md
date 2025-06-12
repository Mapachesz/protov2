# Protov2 Voice Assistant

This project provides a simple Spanish voice assistant that uses GPT4All for natural language responses, Coqui TTS for speech synthesis, and Vosk for speech recognition.

## Requirements

Install dependencies from `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

You will also need the Vosk Spanish model placed under `models/vosk-es`.

## Running

Execute the assistant with:

```bash
python main.py
```

## Notes on GPT4All

When importing GPT4All, the library may attempt to load CUDA libraries to enable GPU acceleration. If CUDA is not available on your system, you will see warnings during initialization. These warnings are harmless—GPT4All will fall back to the CPU automatically, and the assistant will continue to work.

