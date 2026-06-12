from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

youtube = build(
    "youtube",
    "v3",
    developerKey=os.getenv("YOUTUBE_API_KEY")
)

def get_videos(query):
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=5,
        type="video"
    )

    response = request.execute()
    return response["items"]