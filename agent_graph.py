import re

def route_prompt(prompt: str):

    p = prompt.lower()

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

    if "what is" in p:
        expr = (
            p.replace("what is", "")
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("divided by", "/")
        )

        return "calculator", expr.strip(), None

    return "rag", prompt, None