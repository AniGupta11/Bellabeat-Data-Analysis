import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_PATH = r"D:/Projects/Bellabeat/Data/Processed/bellabeat_clean.csv"

def run_python_eda():
    df = pd.read_csv(CSV_PATH)

    print(" Dataset loaded successfully!")
    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nSummary Stats:\n", df.describe(include="all"))

    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

    if "total_steps" in df.columns and "calories" in df.columns:
        plt.figure(figsize=(6,4))
        sns.scatterplot(x="total_steps", y="calories", data=df)
        plt.title("Steps vs Calories")
        plt.show()
    else:
        print(" Columns total_steps or calories not found.")

    if "total_minutes_asleep" in df.columns:
        plt.figure(figsize=(6,4))
        sns.histplot(df["total_minutes_asleep"].dropna(), bins=20, kde=True)
        plt.title("Sleep Duration Distribution")
        plt.xlabel("Minutes Asleep")
        plt.show()
    else:
        print(" Column total_minutes_asleep not found.")

    if "activity_date" in df.columns and "total_steps" in df.columns:
        df["weekday"] = pd.to_datetime(df["activity_date"]).dt.day_name()
        plt.figure(figsize=(8,4))
        sns.barplot(x="weekday", y="total_steps", data=df, estimator="mean", errorbar=None)
        plt.title("Average Steps by Weekday")
        plt.xticks(rotation=45)
        plt.show()
    else:
        print(" Columns activity_date or total_steps not found.")

    print(" Python EDA completed successfully.")

if __name__ == "__main__":
    run_python_eda()
