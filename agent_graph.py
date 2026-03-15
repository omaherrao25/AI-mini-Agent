import re

def route_prompt(prompt: str):

    p = prompt.lower()

    if "remember" in p:
        match = re.search(r"remember my (.*) is (.*)", p)
        if match:
            return "memory_save", match.group(1), match.group(2)

    if "what is my" in p:
        match = re.search(r"what is my (.*)\??", p)
        if match:
            return "memory_read", match.group(1), None

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