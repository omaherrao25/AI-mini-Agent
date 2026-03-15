from pydantic import BaseModel
from typing import Dict, Any, Optional

class PromptRequest(BaseModel):
    prompt: str

class AgentResponse(BaseModel):
    original_prompt: str
    chosen_tool: str
    tool_input: Optional[str]
    response: Dict[str, Any]