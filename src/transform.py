import pandas as pd

from typing import Tuple

def transform_life_expectancy(life_expectancy_df: pd.DataFrame, dimensions_df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Merge life expectancy data with country names from dimensions data.
    Returns filtered and average life expectancy DataFrames.
    """
    # Build country code to name mapping from dimensions_df
    country_code_map = dict(zip(dimensions_df['Code'], dimensions_df['Title']))
    
    # Replace country codes with country names
    life_expectancy_df = life_expectancy_df.copy()
    life_expectancy_df['country'] = life_expectancy_df['country_code'].map(country_code_map)
    
    # Filter data for specific years (e.g., 2000 and 2010)
    filtered_df = life_expectancy_df[life_expectancy_df['year'].isin([2000, 2010])]
    
    # Calculate average life expectancy per country
    avg_life_expectancy = life_expectancy_df.groupby('country')['life_expectancy'].mean().reset_index()
    
    return filtered_df, avg_life_expectancy
