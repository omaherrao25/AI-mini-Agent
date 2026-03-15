import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.create_collection("docs")

def add_documents():

    docs = [
        "An AI agent is a system that can perceive its environment and take actions to achieve goals.",
        "AI agents often use tools, memory, and reasoning to solve problems.",
        "Modern AI agents combine LLMs, tools, and workflows to automate tasks."
    ]

    for i, doc in enumerate(docs):

        embedding = model.encode(doc).tolist()

        collection.add(
            documents=[doc],
            embeddings=[embedding],
            ids=[str(i)]
        )

def search_docs(query):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results["documents"]