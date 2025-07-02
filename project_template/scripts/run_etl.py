# etl-pipeline/scripts/run_etl.py

import sys

from etl.extract import extract_data
from etl.load import load_data
from etl.transform import transform_data


def run_etl():
    try:
        # Step 1: Extract data
        data = extract_data()
        print("Data extracted successfully.")

        # Step 2: Transform data
        transformed_data = transform_data(data)
        print("Data transformed successfully.")

        # Step 3: Load data
        load_data(transformed_data)
        print("Data loaded successfully.")

    except Exception as e:
        print(f"An error occurred during the ETL process: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run_etl()
