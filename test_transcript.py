from utils import get_transcript_2, get_summary_2


# Example usage
video_url = "https://www.youtube.com/watch?v=iDRLGmyNWDU"
transcript = get_transcript_2(video_url)
summary = get_summary_2(transcript)

print(transcript)