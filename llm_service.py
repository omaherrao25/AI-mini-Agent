from langchain_community.llms import Ollama

# initialize local LLM
llm = Ollama(model="llama3")

def ask_llm(prompt: str):

    response = llm.invoke(prompt)

    return {
        "answer": response
    }