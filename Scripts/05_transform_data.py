import pandas as pd
import os

PROCESSED_PATH = r"D:/Projects/Bellabeat/Data/Processed/"
INPUT_FILE = os.path.join(PROCESSED_PATH, "bellabeat_clean.csv")
OUTPUT_FILE = os.path.join(PROCESSED_PATH, "bellabeat_analysis_ready.csv")

def transform_data():
    df = pd.read_csv(INPUT_FILE)

    df["activity_date"] = pd.to_datetime(df["activity_date"])

    df["weekday"] = df["activity_date"].dt.day_name()
    df["is_weekend"] = df["activity_date"].dt.weekday >= 5

    if "total_minutes_asleep" in df.columns:
        df["sleep_hours"] = df["total_minutes_asleep"] / 60

    active_cols = ["very_active_minutes", "fairly_active_minutes", "lightly_active_minutes"]
    df["total_active_minutes"] = df[active_cols].sum(axis=1, skipna=True)

    if "sedentary_minutes" in df.columns:
        df["sedentary_hours"] = df["sedentary_minutes"] / 60

    if "total_time_in_bed" in df.columns and "total_minutes_asleep" in df.columns:
        df["sleep_efficiency"] = df["total_minutes_asleep"] / df["total_time_in_bed"]

    if "bmi" in df.columns:
        def bmi_category(bmi):
            if pd.isna(bmi): return None
            if bmi < 18.5: return "Underweight"
            elif 18.5 <= bmi < 24.9: return "Normal"
            elif 25 <= bmi < 29.9: return "Overweight"
            else: return "Obese"
        df["bmi_category"] = df["bmi"].apply(bmi_category)

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Transformed dataset saved at {OUTPUT_FILE}")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())

if __name__ == "__main__":
    transform_data()
