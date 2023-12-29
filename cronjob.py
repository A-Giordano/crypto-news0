from utils import get_new_video_id, get_transcript, get_summary, send_message
from config import SEARCH_MIN_TIMEDELTA

if __name__ == "__main__":
    videos_ids = get_new_video_id(SEARCH_MIN_TIMEDELTA)
    for video_id in videos_ids:
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"video_url: {video_url}")
        youtube_transcript = get_transcript(video_url)
        print(f"youtube_transcript: {youtube_transcript[0].page_content[:50]}")

        summary = get_summary(youtube_transcript)
        print(f"summary: {summary[:50]}")

        print("got summary")
        send_message(summary)
        print("sent summary")


