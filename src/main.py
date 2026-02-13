from extract import extract_from_ghoapi
from transform import avg_expectancy_per_country
from db_connection import engine

LIFE_EXPECTANCY_URL = "https://ghoapi.azureedge.net/api/WHOSIS_000001"
DIMENSION_URL = "https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues"

if __name__ == "__main__":
    df_expectancy = extract_from_ghoapi(LIFE_EXPECTANCY_URL)

    df = avg_expectancy_per_country(df_expectancy, extract_from_ghoapi(DIMENSION_URL))
    
    df.to_sql('zenysis', engine, if_exists='append', index=False)