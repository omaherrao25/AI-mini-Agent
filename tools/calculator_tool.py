def calculator_tool(expression: str):

    try:
        result = eval(expression) # Evaluates the mathematical expression provided as input.
        return {
            "result": result
        }

    except:
        return {
            "error": "Invalid expression"
        }