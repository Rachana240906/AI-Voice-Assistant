#pip install -q TTS
#pip install -U numpy==1.21
#pip install -q openai-whisper
#pip install -q gradio
#pip install -q openai


import whisper
import gradio as gr 
import openai
from TTS.api import TTS
TTS.list_models()
['tts_models/multilingual/multi-dataset/your_tts',
 'tts_models/bg/cv/vits',
 'tts_models/cs/cv/vits',
 'tts_models/da/cv/vits',
 'tts_models/et/cv/vits',
 'tts_models/ga/cv/vits',
 'tts_models/en/ek1/tacotron2',
 'tts_models/en/ljspeech/tacotron2-DDC',
 'tts_models/en/ljspeech/tacotron2-DDC_ph',
 'tts_models/en/ljspeech/glow-tts',
 'tts_models/en/ljspeech/speedy-speech',
 'tts_models/en/ljspeech/tacotron2-DCA',
 'tts_models/en/ljspeech/vits',
 'tts_models/en/ljspeech/vits--neon',
 'tts_models/en/ljspeech/fast_pitch',
 'tts_models/en/ljspeech/overflow',
 'tts_models/en/ljspeech/neural_hmm',
 'tts_models/en/vctk/vits',
 'tts_models/en/vctk/fast_pitch',
 'tts_models/en/sam/tacotron-DDC',
 'tts_models/en/blizzard2013/capacitron-t2-c50',
 'tts_models/en/blizzard2013/capacitron-t2-c150_v2',
 'tts_models/es/mai/tacotron2-DDC',
 'tts_models/es/css10/vits',
 'tts_models/fr/mai/tacotron2-DDC',
 'tts_models/fr/css10/vits',
 'tts_models/uk/mai/glow-tts',
 'tts_models/uk/mai/vits',
 'tts_models/zh-CN/baker/tacotron2-DDC-GST',
 'tts_models/nl/mai/tacotron2-DDC',
 'tts_models/nl/css10/vits',
 'tts_models/de/thorsten/tacotron2-DCA',
 'tts_models/de/thorsten/vits',
 'tts_models/de/thorsten/tacotron2-DDC',
 'tts_models/de/css10/vits-neon',
 'tts_models/ja/kokoro/tacotron2-DDC',
 'tts_models/tr/common-voice/glow-tts',
 'tts_models/it/mai_female/glow-tts',
 'tts_models/it/mai_female/vits',
 'tts_models/it/mai_male/glow-tts',
 'tts_models/it/mai_male/vits',
 'tts_models/ewe/openbible/vits',
 'tts_models/hau/openbible/vits',
 'tts_models/lin/openbible/vits',
 'tts_models/tw_akuapem/openbible/vits',
 'tts_models/tw_asante/openbible/vits',
 'tts_models/yor/openbible/vits',
 'tts_models/hu/css10/vits',
 'tts_models/el/cv/vits',
 'tts_models/fi/css10/vits',
 'tts_models/hr/cv/vits',
 'tts_models/lt/cv/vits',
 'tts_models/lv/cv/vits',
 'tts_models/mt/cv/vits',
 'tts_models/pl/mai_female/vits',
 'tts_models/pt/cv/vits',
 'tts_models/ro/cv/vits',
 'tts_models/sk/cv/vits',
 'tts_models/sl/cv/vits',
 'tts_models/sv/cv/vits',
 'tts_models/ca/custom/vits',
 'tts_models/fa/custom/glow-tts']

model_name = TTS.list_models()[9]
tts = TTS(model_name)
tts.tts_to_file(text="I love playing Chess", file_path="output.wav")
from IPython.display import Audio, display

display(Audio('output.wav', autoplay=True))
model = whisper.load_model("medium")
openai.api_key = 'sbdk---'
def voice_chat(user_voice):

    messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
    ]
          
    
    user_message = model.transcribe(user_voice)["text"]

    #reply = user_message

    messages.append(
        {"role": "user", "content": user_message},
    )

    print(messages)

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    
    reply = chat.choices[0].message.content
    
    messages.append({"role": "assistant", "content": reply})

    tts.tts_to_file(text=reply, file_path="output.wav")

    return(reply, 'output.wav')
text_reply = gr.Textbox(label="ChatGPT Text")
voice_reply = gr.Audio('output.wav')

gr.Interface(
    title = 'AI Voice Assistant with ChatGPT AI', 
    fn=voice_chat, 
    inputs=[
        gr.inputs.Audio(source="microphone", type="filepath")
    ],

    outputs=[
        text_reply,  voice_reply
    ], live = True).launch(debug = True)
