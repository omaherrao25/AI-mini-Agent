# 🤖 AI Agent Backend -- FastAPI POC

This project implements a **simple AI agent backend** using
**FastAPI**.\
The agent receives user prompts, analyzes the intent, and routes the
request to the appropriate internal tool.

Supported tools:

-   🧮 **Calculator Tool** -- Evaluates simple math expressions
-   💾 **Memory Tool** -- Stores and retrieves user information using a
    database
-   📚 **RAG Tool** -- Retrieves relevant knowledge from a vector
    database

This project demonstrates backend API development, database interaction,
AI-agent routing, and Retrieval Augmented Generation (RAG).

------------------------------------------------------------------------

# 🚀 Tech Stack

-   Python 3.10+
-   FastAPI
-   Pydantic
-   SQLAlchemy
-   SQLite / PostgreSQL
-   ChromaDB (Vector Database)
-   Sentence Transformers (Embeddings)

------------------------------------------------------------------------

# 🧠 System Architecture

User Prompt\
↓\
FastAPI API\
↓\
Agent Router\
↓\
Calculator Tool \| Memory Tool \| RAG Tool\
↓\
Database / Vector Database

------------------------------------------------------------------------

# 📁 Project Structure

ai-agent-backend/

├── main.py\
├── database.py\
├── models.py\
├── schemas.py

├── tools/\
│ ├── calculator_tool.py\
│ ├── memory_tool.py\
│ └── rag_tool.py

├── vector_store.py\
├── memory.sql\
├── requirements.txt\
└── README.md

------------------------------------------------------------------------

# ⚙️ Setup Instructions

## 1. Create Virtual Environment

python -m venv venv

Activate:

Windows: venv`\Scripts`{=tex}`\activate`{=tex}

Mac/Linux: source venv/bin/activate

------------------------------------------------------------------------

## 2. Install Dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## 3. Run Server

uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

------------------------------------------------------------------------

# 🧪 Testing the API

Open Swagger UI:

http://127.0.0.1:8000/docs

Use endpoint:

POST /agent/query

------------------------------------------------------------------------

# 📌 Example Prompts

### Calculator

{ "prompt": "What is 10 plus 5?" }

### Save Memory

{ "prompt": "Remember my cat's name is Fluffy" }

### Recall Memory

{ "prompt": "What is my cat's name?" }

### RAG Query

{ "prompt": "Explain AI agents" }

------------------------------------------------------------------------

# 🗄 Database

Memory is stored as key-value pairs.

SQL Schema:

CREATE TABLE memory ( id SERIAL PRIMARY KEY, key VARCHAR(255) UNIQUE,
value VARCHAR(255) );

------------------------------------------------------------------------

# ❗ Error Handling

If the agent cannot match a prompt to a tool:

{ "error": "I do not have a tool for that." }

------------------------------------------------------------------------

# ⚠️ Security Note

The calculator uses Python eval() for simplicity.\
In production systems, this should be replaced with a safe expression
parser.

------------------------------------------------------------------------

# 🚀 Future Improvements

-   Replace rule-based routing with LLM-based intent detection
-   Add authentication and multi-user memory
-   Use PostgreSQL for production deployment
-   Add Redis caching
-   Containerize using Docker

------------------------------------------------------------------------

# 👨‍💻 Author

Om Aherrao
