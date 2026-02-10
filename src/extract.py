import requests
import pandas as pd

# Example: Extract Life Expectancy at Birth (indicator: WHOSIS_000001)
API_URL = "https://ghoapi.azureedge.net/api/WHOSIS_000001"

def extract_life_expectancy():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()['value']
    df = pd.DataFrame(data)
    return df

