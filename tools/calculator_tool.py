def calculator_tool(expression: str):

    try:
        result = eval(expression)

        return {
            "result": result
        }

    except:
        return {
            "error": "Invalid expression"
        }