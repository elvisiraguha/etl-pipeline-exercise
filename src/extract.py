import requests
import pandas as pd

"""Module for extracting data from a given API URL."""

def extract_from_ghoapi(api_url):
    """
    Extracts data from the given API URL and returns it as a DataFrame.

    Args:
        api_url (str): The API endpoint URL.

    Returns:
        pd.DataFrame: DataFrame containing the extracted data.
    """
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
    data = response.json()['value']
    df = pd.DataFrame(data)
    return df
