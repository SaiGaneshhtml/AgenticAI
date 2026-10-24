import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() 

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 1. The memory starts with exactly 1 item: The System Rule
chat_history = [
    {"role": "system", "content": "You are a helpful coding assistant. Keep answers to 1 sentence."}
]

print("🤖 Simple Chat ready! (Type 'quit' to exit)")

while True:
    # 2. Get the user's text
    user_text = input("\n👨‍💻 You: ")
    if user_text.lower() == 'quit':
        break
        
    # 3. APPEND USER: We add your question to the list
    chat_history.append({"role": "user", "content": user_text})
    
    print(f"[DEBUG] The array now has {len(chat_history)} items. Sending to API...")
    
    # 4. SEND TO API: The AI reads the entire list top-to-bottom
    response = client.chat.completions.create(
        model="gemini-3.5-flash-lite", 
        messages=chat_history
    )
    
    # 5. GET AI REPLY: We extract just the text string from the response
    ai_reply = response.choices[0].message.content
    print(f"🤖 AI: {ai_reply}")
    
    # 6. APPEND AI: We add the AI's answer to the list so it remembers it for next time
    chat_history.append({"role": "assistant", "content": ai_reply})
    
    print(f"[DEBUG] The array now has {len(chat_history)} items. Ready for your next question.")