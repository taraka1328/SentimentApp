from googleapiclient.discovery import build
import os
API_KEY = os.environ.get("API_KEY_VALUE")

def fetch_comments_all(video_id):
    """
    Fetch ALL top-level comments from a YouTube video.

    Args:
        video_id (str): YouTube video ID

    Returns:
        list: List of comment texts
    """

    youtube = build(
        "youtube",
        "v3",
        developerKey=API_KEY
    )

    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )

        response = request.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        # Move to next page
        next_page_token = response.get("nextPageToken")

        # No more pages → stop
        if not next_page_token:
            break

    return comments
