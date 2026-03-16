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

from tools.llm_tool import llm_tool

add_documents()

Base.metadata.create_all(bind=engine) # Create database tables automatically based on the defined SQLAlchemy models.

app = FastAPI(title="AI Agent Backend") # Initialize FastAPI application with the title "AI Agent Backend".

# DB Dependency
def get_db():

    db = SessionLocal() # Open a new database session.

    try:
        yield db # dependency function that provides a database session to the route handlers

    finally:
        db.close()


@app.post("/agent/query", response_model=AgentResponse) # Define a POST endpoint that returns an AgentResponse.
def agent_query(request: PromptRequest, db: Session = Depends(get_db)): # Define the route handler for the /agent/query endpoint

    tool, input1, input2 = route_prompt(request.prompt) # Route the incoming prompt and extract the necessary inputs for that tool.

    try:

        # MEMORY SAVE
        if tool == "memory_save":
            result = save_memory(db, input1, input2)

        # MEMORY READ
        elif tool == "memory_read":
            result = get_memory(db, input1)

        # CALCULATOR
        elif tool == "calculator":
            result = calculator_tool(input1)

        # RAG TOOL
        elif tool == "rag":
            result = rag_tool(input1)

        # LLM TOOL (Ollama)
        elif tool == "llm":
            result = llm_tool(input1)

        # UNKNOWN TOOL
        else:
            return {"error": "I do not have a tool for that."}

    except Exception as e:
        return {"error": str(e)}

    return {
        "original_prompt": request.prompt,
        "chosen_tool": tool,
        "tool_input": input1,
        "response": result
    }