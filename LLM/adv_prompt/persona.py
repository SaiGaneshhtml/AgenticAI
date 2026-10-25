import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

system_prompt = """  
"""

# 1. Initialize the conversation history with the system prompt
messages = [
    {"role": "system", "content": system_prompt}
]

print("Chat started! Type 'exit' or 'quit' to stop.\n")

# 2. Create the interactive loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Chat ended.")
        break
        
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    
    # 3. Call the API, asking it to return JSON format
    response = client.chat.completions.create(
        model="gemini-3.8-flash", # Use a standard model name
        messages=messages,
        response_format={ "type": "json_object" } # Request JSON output
    )
    
    # Parse the JSON response
    try:
        raw_content = response.choices[0].message.content
        # Assuming the model returns something like {"response": "..."}
        # If it just returns plain text despite the flag, we handle that too.
        parsed_response = json.loads(raw_content)
        
        # Try to extract the message text from common keys
        if "response" in parsed_response:
            bot_reply = parsed_response["response"]
        elif "message" in parsed_response:
             bot_reply = parsed_response["message"]
        else:
            bot_reply = raw_content # Fallback if structure is unexpected
            
    except json.JSONDecodeError:
        bot_reply = response.choices[0].message.content

    print(f"Friend: {bot_reply}\n")
    
    # Add the assistant's reply to the history so it remembers context
    messages.append({"role": "assistant", "content": bot_reply})