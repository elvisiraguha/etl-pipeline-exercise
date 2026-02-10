import pandas as pd
from extract import extract_life_expectancy

if __name__ == "__main__":
    df = extract_life_expectancy()
    print(df.head())
    # Optionally save to CSV
    df.to_csv("life_expectancy_raw.csv", index=False)