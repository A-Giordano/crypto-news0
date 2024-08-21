from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split("?v=")[1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as e:
        return f"Error: {e}"

# Example usage
video_url = "https://www.youtube.com/watch?v=iDRLGmyNWDU"
transcript = get_youtube_transcript(video_url)
print(transcript)