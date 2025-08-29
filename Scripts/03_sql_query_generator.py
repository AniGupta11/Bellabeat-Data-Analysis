import sqlite3
import pandas as pd

DB_PATH = "bellabeat.db"
CSV_PATH = r"D:/Projects/Bellabeat/Data/Processed/bellabeat_clean.csv"
SQL_SCRIPT_PATH = "sql/bellabeat_analysis.sql"

def run_sql_analysis():

    conn = sqlite3.connect(DB_PATH)
    df = pd.read_csv(CSV_PATH)
    df.to_sql("bellabeat", conn, if_exists="replace", index=False)

    queries = {
        "avg_steps_per_user": """
            SELECT Id, AVG(TotalSteps) AS avg_steps
            FROM bellabeat
            GROUP BY Id;
        """,
        "avg_sleep_per_user": """
            SELECT Id, AVG(TotalMinutesAsleep) AS avg_sleep_minutes
            FROM bellabeat
            GROUP BY Id;
        """,
        "avg_calories_by_weekday": """
            SELECT strftime('%w', activity_date) AS weekday,
                   AVG(Calories) AS avg_calories
            FROM bellabeat
            GROUP BY weekday;
        """,
        "top_active_users": """
            SELECT Id, SUM(TotalSteps) AS total_steps
            FROM bellabeat
            GROUP BY Id
            ORDER BY total_steps DESC
            LIMIT 5;
        """,
        "sleep_vs_calories": """
            SELECT AVG(TotalMinutesAsleep) AS avg_sleep,
                   AVG(Calories) AS avg_calories
            FROM bellabeat
            GROUP BY Id;
        """
    }

    with open(SQL_SCRIPT_PATH, "w") as f:
        for name, query in queries.items():
            f.write(f"-- {name}\n{query}\n\n")

    print(f" SQL queries written to {SQL_SCRIPT_PATH}")

if __name__ == "__main__":
    run_sql_analysis()
