from analyzer.fetch_comments import fetch_comments_all
from analyzer.sentiment import predict_sentiment
from analyzer.save_result import save_to_csv
def analyze_video(video_id):
    """
    Full pipeline:
    video_id -> comments -> sentiment results
    """

    # 1. Fetch comments
    comments = fetch_comments_all(video_id)

    if not comments:
        return []

    # 2. Predict sentiment
    results = predict_sentiment(comments)
    save_to_csv(results)
    return results
