import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HISTORY_FILE = BASE_DIR / "data" / "incident_history.csv"


def save_incident(record):

    print("Saving record:", record)
    print("Saving to:", HISTORY_FILE)

    if HISTORY_FILE.exists():
        df = pd.read_csv(HISTORY_FILE)
    else:
        df = pd.DataFrame()

    df = pd.concat(
        [df, pd.DataFrame([record])],
        ignore_index=True
    )

    df.to_csv(
        HISTORY_FILE,
        index=False
    )


def load_history():

    print("Loading from:", HISTORY_FILE)

    if HISTORY_FILE.exists():
        return pd.read_csv(HISTORY_FILE)

    return pd.DataFrame(
        columns=[
            "timestamp",
            "threat",
            "priority",
            "recommendation"
        ]
    )