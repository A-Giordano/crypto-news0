from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse

from utils import get_summary, send_message, get_transcript

app = FastAPI()

@app.post("/transcript")
async def get_transcript(request: Request):
    # Extract JSON body from the request. Expected format: {"url": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"}
    data = await request.json()
    video_url = data.get("url")

    transcript = get_transcript(video_url)
    summary = get_summary(transcript)
    await send_message(summary)

    print("Success!!")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Successfully sent message"},
    )
