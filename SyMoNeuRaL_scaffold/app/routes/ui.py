from fastapi import APIRouter, HTTPException
from app.models import TextRequest, TextResponse

router = APIRouter()

@router.get("/text", response_model=TextResponse)
def get_text(message: str):
    reply = f"SyMoNeuRaL (stub) received: {message}"
    return TextResponse(response=reply, meta={"source":"ui.text.get"})

@router.post("/message", response_model=TextResponse)
def post_message(req: TextRequest):
    if not req.message:
        raise HTTPException(status_code=400, detail="message required")
    reply = f"SyMoNeuRaL (stub) processed: {req.message}"
    meta={"processed":True,"context_keys":list(req.context.keys()) if req.context else []}
    return TextResponse(response=reply, meta=meta)
