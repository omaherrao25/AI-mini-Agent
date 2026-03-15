import re

def route_prompt(prompt: str): # used for routing the incoming prompt to the appropriate tool based on its content.

    p = prompt.lower()

    # MEMORY SAVE
    if "remember" in p:
        match = re.search(r"remember my (.*) is (.*)", p)
        if match:
            return "memory_save", match.group(1), match.group(2)

    # MEMORY READ
    if "what is my" in p:
        match = re.search(r"what is my (.+?)(\?|$)", p)
        if match:
            key = match.group(1).strip()
            return "memory_read", key, None

    # CALCULATOR
    if "what is" in p:
        expr = (
            p.replace("what is", "")
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("divided by", "/")
        )

        return "calculator", expr.strip(), None

    return "rag", prompt, None # If the prompt does not match, it defaults to using the RAG tool, passing the entire prompt as input.