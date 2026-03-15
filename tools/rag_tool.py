from vector_store import search_docs

def rag_tool(query):

    docs = search_docs(query)

    return {
        "documents": docs
    }