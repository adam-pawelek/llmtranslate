from openai import OpenAI

# init the client but point it to TGI
client = OpenAI(
    base_url="http://localhost:8080/v1/",
    api_key="-"
)

chat_completion = client.chat.completions.create(
    model="tgi",
    messages=[
        {"role": "system", "content": "You are a helpful assistant." },
        {"role": "user", "content": "What is deep learning?"}
    ],
    stream=True
)

# iterate and print stream
for message in chat_completion:
    print(message)