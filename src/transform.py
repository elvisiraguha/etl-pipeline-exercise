"""
Transform life expectancy data by mapping country codes to country names using WHO API.
"""

import pandas as pd
import requests

# Load the data
df = pd.read_csv('life_expectancy_raw.csv')

# Fetch country code to name mapping from WHO API
response = requests.get('https://ghoapi.azureedge.net/api/DIMENSION/COUNTRY/DimensionValues')
country_data = response.json()['value']
country_code_map = {item['Code']: item['Title'] for item in country_data}

# Replace country codes with country names
df['country'] = df['country_code'].map(country_code_map)

# Filter data for specific years (e.g., 2000 and 2010)
filtered_df = df[df['year'].isin([2000, 2010])]

# Calculate average life expectancy per country
avg_life_expectancy = df.groupby('country')['life_expectancy'].mean().reset_index()

# Save transformed data
filtered_df.to_csv('filtered_life_expectancy.csv', index=False)
avg_life_expectancy.to_csv('avg_life_expectancy.csv', index=False)