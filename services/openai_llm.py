import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(context, query):
    messages = [
        {"role": "system", "content": f"You are an AI doctor. Use this context:\n{context}"},
        {"role": "user", "content": query}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response['choices'][0]['message']['content']
