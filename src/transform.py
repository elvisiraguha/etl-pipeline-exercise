import pandas as pd

def avg_expectancy_per_country(life_expectancy_df: pd.DataFrame, dimensions_df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute average life expectancy per country.
    """

    country_code_map = dict(zip(dimensions_df['Code'], dimensions_df['Title']))
    
    life_expectancy_df = life_expectancy_df.copy()
    life_expectancy_df['country'] = life_expectancy_df['SpatialDim'].map(country_code_map)
    
    avg_life_expectancy = life_expectancy_df.groupby('country')['NumericValue'].mean().reset_index()
    
    return avg_life_expectancy
