from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
model_name=os.getenv("MODEL_NAME")
environment=os.getenv("ENVIRONMENT")

print("Environment:", environment)
print("Model:", model_name)

if api_key:
    print("Groq API Key loaded successfully!")
    print("Key starts with:", api_key[:8]+ "...")
else:
    print("Key not found.")