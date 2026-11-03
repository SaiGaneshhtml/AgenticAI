from transformers import pipeline

url = "https://imgs.search.brave.com/BXdOy1cJJE_3zjm4y44yKVIp2hhnaoy4qr355zfxrmY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNTUv/MTYzLzA4NC9zbWFs/bC9kZWxpY2F0ZS1w/aW5rLWZsb3dlcnMt/d2l0aC1zb2Z0LWZv/Y3VzLWFuZC1ibHVy/cmVkLWJhY2tncm91/bmQtbmF0dXJlLWJl/YXV0eS1hbmQtc2Vy/ZW5pdHktY29uY2Vw/dC1waG90by5qcGVn"
question = "What is it?"

pipe = pipeline("image-text-to-text", model="HuggingFaceTB/SmolVLM-500M-Instruct")

messages = [{"role": "user", "content": [
    {"type": "image", "url": url},
    {"type": "text", "text": question},
]}]

out = pipe(text=messages, max_new_tokens=60)
print(out[0]["generated_text"][-1]["content"])

#o/p be like 
# [transformers] Image decoding with `torchvision` is deprecated and will be removed in future versions .Please install `torchcodec>=0.16.0` instead. 
#  The image is a flower.
# (prompt) ganesh@SG:/mnt/c/Users/sai/Downloads/AgenticAIwithpython/LLM/hugging_face$ 