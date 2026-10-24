import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the secret GEMINI_API_KEY from your root .env file
load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        # SYSTEM PROMPT: Sets the strict rules and persona for the AI
        {
            "role": "system", 
            "content": "You are an expert programmer. You must ONLY answer questions related to coding, software development, and technology. If the user asks about anything outside of this scope (like history, food, or sports), you must politely refuse to answer. sorry i can't"
        },
        # USER PROMPT: What the user is actually asking
        # {
        #     "role": "user", 
        #     "content": "Can you give me a recipe for chocolate cake?"
        # },
        {
            "role": "user", 
            "content": "suggest me 1 best yt channel for agentic ai"
        },
    ]
)

print("Response:\n", response.choices[0].message.content)