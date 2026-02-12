import pandas as pd
from extract import extract_from_ghoapi
from transform import transform_life_expectancy

LIFE_EXPECTANCY_URL = "https://ghoapi.azureedge.net/api/WHOSIS_000001"
DIMENSION_URL = "https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues"

if __name__ == "__main__":
    df_expectancy = extract_from_ghoapi(LIFE_EXPECTANCY_URL)
    print(df_expectancy.head())
    df, df2 = transform_life_expectancy(df_expectancy, extract_from_ghoapi(DIMENSION_URL))
    print(df.head())
    print(df2.head())
    # Optionally save to CSV
    # df.to_csv("life_expectancy_raw.csv", index=False)