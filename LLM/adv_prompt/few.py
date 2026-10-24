import os
from pydoc import html
from dotenv import load_dotenv
from openai import OpenAI

# Load the secret GEMINI_API_KEY from your root .env file
load_dotenv() 
#few-shot prompt mean given to the model with few examples.
# 
# 
# The model is expected to generate a response based solely on the prompt provided,
#  without any prior context or examples to guide its output.
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
            "content": """You are an expert programmer. You must ONLY answer questions related to coding, software development, and technology. If the user asks about anything outside of this scope (like history, food, or sports),"
            " you must politely refuse to answer. sorry i can't
              example 
                user: who is srk
                assistant: Sorry, I can't provide biographical information about celebrities or non-tech topics. However, I can help you with the HTML code structure you requested:
                
                user: Give me a simple HTML h1 line with a small 2 line paragraph below it.using <p/>
                assistant: sorry I can't provide biographical information about celebrities or non-tech topics. However, I can help you with the HTML code structure you requested:
                  """
        },

        # USER PROMPT: What the user is actually asking
        # {
        #     "role": "user", 
        #     "content": "Can you give me a recipe for chocolate cake?"
        # },

        {
            "role": "user", 
            "content": "Give me a simple HTML h1 line with a small 2 line paragraph below it.using <p/> who is srk"
        },
    ]
)

print("Response:\n", response.choices[0].message.content)

# **o/p**
# (prompt) ganesh@SG:/mnt/c/Users/sai/Downloads/AgenticAIwithpython/LLM/adv_prompt$ python3 few.py 
# Response:
#  Sorry, I can't provide biographical information about celebrities or non-tech topics. However, I can help you with the HTML code structure you requested:

# ```html
# <h1>This is a Heading</h1>
# <p>
#   This is the first line of the paragraph.<br>
#   This is the second line of the paragraph.
# </p>
# ```