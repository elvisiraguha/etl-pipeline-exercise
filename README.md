# ETL Pipeline for WHO GHO OData API

This project implements a simple ETL (Extract, Transform, Load) pipeline in Python. The pipeline extracts health-related data from the WHO GHO OData API, applies basic transformations (such as replacing country codes with names and calculating averages), and loads the processed data into a PostgreSQL database.

## Installation

1. Clone the repository:  
    ```bash
    git clone https://github.com/elvisiraguha/etl-pipeline-exercise
    ```

2. Use a Python virtual environment.

3. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your PostgreSQL database and update the connection settings in the configuration file or environment variables.

5. Run the main script:  
    ```bash
    python src/main.py
    ```

## Goal

The goal of this ETL pipeline is to automate the process of collecting, transforming, and storing WHO health data for further analysis or reporting.