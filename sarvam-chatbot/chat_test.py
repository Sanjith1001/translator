from src.chat import chat

history = []

print("Testing Hindi...")
reply, lang, history = chat("नमस्ते! आप कैसे हैं?", history=history)
print(f"Detected: {lang}")
print(f"Reply: {reply}\n")

print("Testing Tamil...")
reply, lang, history = chat("வணக்கம்! நீங்கள் எப்படி இருக்கீர்கள்?", history=history)
print(f"Detected: {lang}")
print(f"Reply: {reply}\n")

print("Testing Hinglish...")
reply, lang, history = chat("Yaar, kya chal raha hai?", history=history)
print(f"Detected: {lang}")
print(f"Reply: {reply}")