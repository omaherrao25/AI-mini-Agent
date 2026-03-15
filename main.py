from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
import models

from schemas import PromptRequest, AgentResponse

from tools.calculator_tool import calculator_tool
from tools.memory_tool import save_memory, get_memory
from tools.rag_tool import rag_tool

from agent_graph import route_prompt

from vector_store import add_documents

add_documents()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Agent Backend")


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.post("/agent/query", response_model=AgentResponse)
def agent_query(request: PromptRequest, db: Session = Depends(get_db)):

    tool, input1, input2 = route_prompt(request.prompt)

    if tool == "memory_save":
        result = save_memory(db, input1, input2)

    elif tool == "memory_read":
        result = get_memory(db, input1)

    elif tool == "calculator":
        result = calculator_tool(input1)

    elif tool == "rag":
        result = rag_tool(input1)

    else:
        return {"error": "I do not have a tool for that."}

    return {
        "original_prompt": request.prompt,
        "chosen_tool": tool,
        "tool_input": input1,
        "response": result
    }