import os
import pandas as pd

def save_to_csv(results, filename="results.csv"):
    """
    Save sentiment results to a CSV file.

    Args:
        results (list of dicts)
        filename (str)
    """

    if not results:
        return None

    # Convert to DataFrame
    df = pd.DataFrame(results)

    # Create data directory if missing
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "..", "data")
    os.makedirs(DATA_DIR, exist_ok=True)

    file_path = os.path.join(DATA_DIR, filename)

    # Save CSV
    df.to_csv(file_path, index=False, encoding="utf-8")

    return file_path
