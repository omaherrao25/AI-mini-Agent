from pydantic import BaseModel
from typing import Dict, Any, Optional

class PromptRequest(BaseModel): # Defines the structure of the incoming request for the agent query.
    prompt: str

class AgentResponse(BaseModel): # Defines the structure of the response returned by the agent query.
    original_prompt: str
    chosen_tool: str
    tool_input: Optional[str]
    response: Dict[str, Any]