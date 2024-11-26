import pandas as pd
from google.cloud import storage, bigquery
from config.settings import RAW_DATA_BUCKET, PROCESSED_DATA_BUCKET, BQ_PROJECT_ID, BQ_DATASET, BQ_TABLE
from transform import transform_data
import io

def load_gcs_file(bucket_name, file_name):
    from google.api_core.exceptions import NotFound

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        data = blob.download_as_text()  # Download file content as text
        return pd.read_csv(io.StringIO(data))  # Use io.StringIO instead of pandas.compat.StringIO
    except NotFound:
        print(f"Error: File {file_name} not found in bucket {bucket_name}.")
        raise

def upload_to_gcs(bucket_name, file_name, df):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(df.to_csv(index=False), content_type="text/csv")

def load_to_bigquery(df):
    client = bigquery.Client()
    table_id = f"{BQ_PROJECT_ID}.{BQ_DATASET}.{BQ_TABLE}"
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  # Wait for the job to complete

def main():
    # Step 1: Extract raw data from GCS
    file_name = "emissions_sample.csv"
    raw_df = load_gcs_file(RAW_DATA_BUCKET, file_name)
    print("Raw Data Loaded")

    # Step 2: Transform data
    transformed_df = transform_data(raw_df)
    print("Data Transformed")

    # Step 3: Load transformed data back to GCS
    processed_file_name = "processed_emissions.csv"
    upload_to_gcs(PROCESSED_DATA_BUCKET, processed_file_name, transformed_df)
    print(f"Transformed Data Uploaded to GCS: {processed_file_name}")

    # Step 4: Load transformed data to BigQuery
    load_to_bigquery(transformed_df)
    print(f"Data Loaded to BigQuery Table: {BQ_TABLE}")

if __name__ == "__main__":
    main()
