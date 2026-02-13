import requests
import pandas as pd

def extract_from_ghoapi(api_url):
    """
    Extract data from the given API URL and return as a DataFrame.
    """
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    data = response.json()['value']
    df = pd.DataFrame(data)
    return df
