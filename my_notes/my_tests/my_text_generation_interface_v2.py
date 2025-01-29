import os

from huggingface_hub import InferenceClient

client = InferenceClient(api_key=os.getenv("YOUR_HF_TOKEN"))

schema = {
    "properties": {
        "location": {"title": "Location", "type": "string"},
        "activity": {"title": "Activity", "type": "string"},
        "animals_seen": {
            "maximum": 5,
            "minimum": 1,
            "title": "Animals Seen",
            "type": "integer",
        },
        "animals": {"items": {"type": "string"}, "title": "Animals", "type": "array"},
    },
    "required": ["location", "activity", "animals_seen", "animals"],
    "title": "Animals",
    "type": "object",
}

user_input = "I saw a puppy a cat and a raccoon during my bike ride in the park"
resp = client.text_generation(
    f"convert to JSON: 'f{user_input}'. please use the following schema: {schema}",
    model="meta-llama/Llama-3.2-1B-Instruct",
    max_new_tokens=100,
    seed=42,
    grammar={"type": "json", "value": schema},
)

print(resp)
# { "activity": "bike ride", "animals": ["puppy", "cat", "raccoon"], "animals_seen": 3, "location": "park" }
