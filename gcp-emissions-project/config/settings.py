import os
from dotenv import load_dotenv


load_dotenv()
# GCS Bucket Details
RAW_DATA_BUCKET = "bkt-raw-data"
PROCESSED_DATA_BUCKET = "bkt-process-data"

# BigQuery Details
BQ_PROJECT_ID = os.getenv("project_id")
BQ_DATASET = "emission_project_dataset"
BQ_TABLE = "emissions_data"

# Other Configurations
CHUNK_SIZE = 1000
