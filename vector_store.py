import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2") # A compact and efficient model for generating sentence embeddings.

client = chromadb.Client() # Initialize the ChromaDB client to manage collections and perform operations on the vector database.

collection = client.create_collection("docs") # ChromaDB stores document embeddings and allows similarity search.

def add_documents():

    docs = [
        "An AI agent is a system that can perceive its environment and take actions to achieve goals.",
        "AI agents often use tools, memory, and reasoning to solve problems.",
        "Modern AI agents combine LLMs, tools, and workflows to automate tasks."
    ]

    for i, doc in enumerate(docs):

        embedding = model.encode(doc).tolist() # Generate a vector representation (embedding)

        collection.add(
            documents=[doc],
            embeddings=[embedding],
            ids=[str(i)]
        ) # Add documents to the ChromaDB collection, storing both the text and its corresponding embedding for later retrieval.

def search_docs(query):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    ) # finds documents that are semantically similar to the user's question

    return results["documents"]