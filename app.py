from chatbot import stream_graph_updates

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the Pydantic model for request validation
class ChatRequest(BaseModel):
    messages: List[str]

# Define the route
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        async def event_stream():
            for message in request.messages:
                async for response in stream_graph_updates(message):
                    yield response

        return StreamingResponse(event_stream(), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    