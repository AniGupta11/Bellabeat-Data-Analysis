import os
import pandas as pd

RAW_DATA_PATH = r"D:/Projects/Bellabeat/Data/Raw/"
OUTPUT_PATH = r"D:/Projects/Bellabeat/Data/Processed/bellabeat_data_dictionary.csv"

def generate_data_dictionary():
    dictionary_records = []

    for file in os.listdir(RAW_DATA_PATH):
        if file.endswith(".csv"):
            file_path = os.path.join(RAW_DATA_PATH, file)
            try:
                df = pd.read_csv(file_path)

                for col in df.columns:
                    dictionary_records.append({
                        "file_name": file,
                        "column_name": col,
                        "dtype": str(df[col].dtype),
                        "non_null_count": df[col].notnull().sum(),
                        "null_count": df[col].isnull().sum(),
                        "unique_values": df[col].nunique()
                    })

            except Exception as e:
                print(f" Error reading {file}: {e}")

    dictionary_df = pd.DataFrame(dictionary_records)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    dictionary_df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"Data dictionary saved at {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_data_dictionary()
