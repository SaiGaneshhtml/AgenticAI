import tiktoken 


#enc = tiktoken.encoding_for_model("gpt-4")
enc_1 = tiktoken.encoding_for_model("gpt-3.5-turbo")
text = "Hello, this is ganesh"
#Tokens: [9906, 11, 420, 374, 25893, 4385]
tokens = enc_1.encode(text)
print("Tokens:", tokens)
decoded_text = enc_1.decode(tokens)
print("Decoded Text:", decoded_text)