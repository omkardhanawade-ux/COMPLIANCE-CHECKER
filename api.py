import os
from dotenv import load_dotenv

load_dotenv(override=True)

print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("PINECONE_API_KEY:", os.getenv("PINECONE_API_KEY"))
print("PINECONE_ENVIRONMENT:", os.getenv("PINECONE_ENVIRONMENT"))