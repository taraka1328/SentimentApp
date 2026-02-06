document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.getElementById("sentimentChart");
    if (!canvas) return;

    const positive = parseInt(canvas.dataset.positive);
    const neutral = parseInt(canvas.dataset.neutral);
    const negative = parseInt(canvas.dataset.negative);

    const data = {
        labels: ["Positive", "Neutral", "Negative"],
        datasets: [{
            label: "Number of Comments",
            data: [positive, neutral, negative],
            backgroundColor: [
                "rgba(0, 128, 0, 0.6)",
                "rgba(255, 165, 0, 0.6)",
                "rgba(255, 0, 0, 0.6)"
            ],
            borderWidth: 1
        }]
    };

    const config = {
        type: "bar",
        data: data,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };

    new Chart(canvas, config);
});
