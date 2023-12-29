from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import JSONResponse

from utils import get_summary, send_message, get_transcript, psw_correct

app = FastAPI()

@app.get("/wakeup")
def wakeup():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Container awake!"},
    )


@app.post("/transcript")
async def transcript(request: Request):
    # Extract JSON body from the request. Expected format: {"url": "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"}
    data = await request.json()
    video_url = data.get("url")
    psw = data.get("psw")
    if not await psw_correct(psw):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"message": "Incorrect PSW"},
        )
    print(f"video_url: {video_url}")
    youtube_transcript = get_transcript(video_url)
    print(f"youtube_transcript: {youtube_transcript[:50]}")

    print("got transcript")
    summary = get_summary(youtube_transcript)
    print("got summary")
    await send_message(summary)
    print("sent summary")

    print("Success!!")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Successfully sent message"},
    )

