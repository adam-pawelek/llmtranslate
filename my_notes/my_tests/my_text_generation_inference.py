import os

from openai import OpenAI

# init the client but point it to TGI
client = OpenAI(
    base_url="https://api-inference.huggingface.co/models/microsoft/Phi-3.5-mini-instruct/v1",
    api_key=os.environ.get("YOUR_HF_TOKEN"),
)

chat_completion = client.chat.completions.create(
    model="microsoft/Phi-3.5-mini-instruct",
	messages=[
		{"role": "system",
		 "content": f"You are a language translator. You should translate text provided by user to the ISO 639-1: {'English'} language. You should return response in this JSON format: {{'translated_text': 'put here content of translated text'}} Don't write additional message like This is translated text just return json format"},
		{"role": "user", "content": "Cześć jak się masz? Ja mam na imię Adam"}
	]
)



print(chat_completion.choices[0].message.content)
# iterate and print stream
