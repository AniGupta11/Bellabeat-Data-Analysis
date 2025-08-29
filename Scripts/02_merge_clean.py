import os
import pandas as pd
import re

RAW_DATA_PATH = r"D:/Projects/Bellabeat/Data/Raw/"
OUTPUT_PATH = r"D:/Projects/Bellabeat/Data/Processed/bellabeat_clean.csv"

def to_snake_case(name: str) -> str:
    """
    Convert column name to snake_case.
    Example: 'TotalSteps' -> 'total_steps'
             'ActivityDate' -> 'activity_date'
    """
    name = name.strip()
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name)  # insert _ before caps
    name = name.replace(" ", "_").replace("-", "_")
    return name.lower()

def clean_and_merge():
    daily_activity = pd.read_csv(os.path.join(RAW_DATA_PATH, "dailyActivity_merged.csv"))
    sleep_day = pd.read_csv(os.path.join(RAW_DATA_PATH, "sleepDay_merged.csv"))
    weight_log = pd.read_csv(os.path.join(RAW_DATA_PATH, "weightLogInfo_merged.csv"))

    daily_activity.columns = [to_snake_case(c) for c in daily_activity.columns]
    sleep_day.columns = [to_snake_case(c) for c in sleep_day.columns]
    weight_log.columns = [to_snake_case(c) for c in weight_log.columns]

    daily_activity["activity_date"] = pd.to_datetime(daily_activity["activity_date"])
    sleep_day["sleep_day"] = pd.to_datetime(sleep_day["sleep_day"])
    weight_log["date"] = pd.to_datetime(weight_log["date"])

    sleep_day = sleep_day.drop_duplicates()
    weight_log = weight_log.drop_duplicates()

    merged = daily_activity.merge(
        sleep_day,
        how="left",
        left_on=["id", "activity_date"],
        right_on=["id", "sleep_day"]
    )

    merged = merged.merge(
        weight_log,
        how="left",
        left_on=["id", "activity_date"],
        right_on=["id", "date"]
    )

    merged = merged.drop(columns=["sleep_day", "date"], errors="ignore")
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    merged.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

    print(f" Cleaned dataset saved at {OUTPUT_PATH}")
    print(f"Rows: {merged.shape[0]}, Columns: {merged.shape[1]}")
    print("Columns:", merged.columns.tolist())

if __name__ == "__main__":
    clean_and_merge()
