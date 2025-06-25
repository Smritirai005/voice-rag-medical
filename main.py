from services.whisper_stt import transcribe_audio
from services.rag import retrieve
from services.openai_llm import ask_gpt

audio_path = "audio/user_input.wav"  # assume you have this file
query = transcribe_audio(audio_path)
print("User asked:", query)

context = "\n".join(retrieve(query))
response = ask_gpt(context, query)

print("\nAI Doctor says:", response)
