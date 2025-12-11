from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class TextRequest(BaseModel):
    message: str = Field(..., example="Hello SyMon")
    context: Optional[Dict[str, Any]] = None

class TextResponse(BaseModel):
    response: str
    meta: Optional[Dict[str, Any]] = None
