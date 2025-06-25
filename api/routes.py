from fastapi import FastAPI, Request
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

@app.post("/twilio-voice")
async def voice_reply(request: Request):
    response = VoiceResponse()
    response.say("Hello. I am your AI doctor. Please describe your symptoms after the beep.")
    response.record(max_length=30, transcribe=True, play_beep=True)
    return str(response)
