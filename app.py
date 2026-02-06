from flask import Flask, render_template, request
from analyzer.pipeline import analyze_video

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    sentiment_counts = {}
    error = None

    if request.method == "POST":
        video_id = request.form.get("video_id")

        try:
            results = analyze_video(video_id)

            if not results:
                error = "No comments found or comments are disabled."
            else:
                sentiment_counts = {
                    "Positive": sum(1 for r in results if r["sentiment"] == "Positive"),
                    "Neutral": sum(1 for r in results if r["sentiment"] == "Neutral"),
                    "Negative": sum(1 for r in results if r["sentiment"] == "Negative"),
                }

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        results=results,
        sentiment_counts=sentiment_counts,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)