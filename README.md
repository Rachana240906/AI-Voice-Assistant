# AI Voice Assistant (Speech-to-Speech with LLM)

## Overview

This project is an end-to-end AI Voice Assistant that enables real-time voice interaction using advanced AI models. It converts speech to text, processes the query using a language model, and generates a spoken response.

The system integrates speech recognition, natural language understanding, and text-to-speech synthesis into a single conversational pipeline.


## Architecture

User Speech → Whisper (STT) → GPT Model → TTS → Voice Output

## Features

* Real-time voice input using microphone
* AI-based response generation using GPT model
* Speech-to-speech interaction
* Text-to-speech voice output
* Web interface using Gradio
* Supports dynamic user queries

## Tech Stack

Programming Language:
Python

Libraries and Models:

* whisper (Speech-to-Text)
* openai (Language Model API)
* TTS (Coqui Text-to-Speech)
* gradio (User Interface)

## Project Structure

AI-Voice-Assistant/
│── main.py
│── output.wav
│── README.md


## Installation

1. Clone the repository
   git clone [https://github.com/your-username/ai-voice-assistant.git](https://github.com/your-username/ai-voice-assistant.git)
   cd ai-voice-assistant

2. Install dependencies
   pip install -q TTS
   pip install -U numpy==1.21
   pip install -q openai-whisper
   pip install -q gradio
   pip install -q openai

## Setup

Replace the OpenAI API key in the code:

openai.api_key = "your-api-key-here"

Do not expose your API key publicly. Use environment variables in production.

## Usage

Run the application:

python main.py

Steps performed by the assistant:

1. Captures user voice input
2. Converts speech to text using Whisper
3. Sends text to GPT model for response generation
4. Converts response to speech using TTS
5. Returns both text and audio output

## How It Works

Speech Recognition:
Audio input is transcribed using Whisper.

AI Processing:
The transcribed text is sent to the GPT model using the OpenAI API.

Speech Synthesis:
The generated response is converted into an audio file using Coqui TTS.

Interface:
Gradio provides a simple web-based interface for interaction.

## Limitations

* Requires internet for API access
* Latency depends on model size and system performance
* No persistent conversation memory

## Future Improvements

* Add conversation memory for context retention
* Upgrade to newer language models
* Improve voice quality using advanced TTS models
* Add multilingual support
* Deploy as a web application
* Reduce response latency

## License

This project is open-source and available under the MIT License.
