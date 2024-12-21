import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings  # Updated import
from pinecone import Pinecone, ServerlessSpec

# Load environment variables from .env file

load_dotenv()

class EmbeddingModel:
    def __init__(self):
        # Ensure environment variables are set
        openai_api_key = os.getenv("OPENAI_API_KEY")
        pinecone_api_key = os.getenv("PINECONE_API_KEY")
        pinecone_environment = os.getenv("PINECONE_ENVIRONMENT")

        if not openai_api_key or not pinecone_api_key or not pinecone_environment:
            raise ValueError("API keys or environment variables are not set.")

        # Initialize OpenAI Embeddings
        self.embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

        # Initialize Pinecone using the correct method
        self.pc = Pinecone(api_key=pinecone_api_key)

        # Create the index if it doesn't exist
        if "compliance-checker" not in self.pc.list_indexes().names():
            self.pc.create_index(
                name="compliancechecker",
                dimension=1536,  # The dimension of your embeddings (e.g., for OpenAI embeddings)
                metric="cosine",  # or "cosine"
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1-aws"
                )
            )

        # Access the index
        self.index = self.pc.index("compliance-checker")

    def generate_embeddings(self, chunks):
        # Use embed_documents instead of embed for a list of chunks
        embeddings = self.embedding_model.embed_documents(chunks)

        # Store the embeddings in Pinecone
        upsert_data = [(str(i), embeddings[i]) for i in range(len(embeddings))]
        self.index.upsert(vectors=upsert_data)

        return embeddings
