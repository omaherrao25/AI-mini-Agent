import ollama


def llm_tool(prompt: str):

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {
        "answer": response["message"]["content"]
    }