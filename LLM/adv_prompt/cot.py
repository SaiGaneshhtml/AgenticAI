import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 1. THE SETUP
system_prompt = """
You are a JS expert. You must return a JSON object with exactly two keys:
"explanation": A short 1-sentence explanation of the logic.
"code": The JavaScript code.
"""

response = client.chat.completions.create(
    model="gemini-3.5-flash-lite", 
    response_format={"type": "json_object"}, # This forces the AI to output valid JSON
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Write a JS function to add two numbers."}
    ]
)

# ---------------------------------------------------------
# HOW THE DATA FLOWS (Read this part carefully)
# ---------------------------------------------------------

# STEP 1: What the AI returns
# The AI does NOT return a Python object. It returns one giant string of text.
raw_ai_string = response.choices[0].message.content

print("--- 1. RAW TEXT FROM AI ---")
print("Data Type:", type(raw_ai_string))
print(raw_ai_string)


# STEP 2: How we parse it
# We use json.loads() to convert that giant text string into a real Python Dictionary.
parsed_dictionary = json.loads(raw_ai_string)

print("\n--- 2. PARSED PYTHON DICTIONARY ---")
print("Data Type:", type(parsed_dictionary))
print(parsed_dictionary)


# STEP 3: How we display it
# Because it is now a Python dictionary, we can ask for specific pieces using the keys.
print("\n--- 3. FINAL CLEAN OUTPUT ---")
print("🧠 Logic:", parsed_dictionary["explanation"])
print("💻 Code:\n", parsed_dictionary["code"])