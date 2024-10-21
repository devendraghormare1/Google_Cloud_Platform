from google.cloud import storage
from google.oauth2 import service_account

# Path to your service account key file
key_path = "E:/workspace/GCP/compute_operations/key.json"  # Change this to your actual path
project_id = "learning-gcp-cyb"  # Replace with your GCP project ID
bucket_name = "python-gcp-bucket-01"  # Replace with a unique bucket name

# Authenticate using the service account key
credentials = service_account.Credentials.from_service_account_file(key_path)

# Create a client for the Google Cloud Storage service
client = storage.Client(credentials=credentials, project=project_id)

# Create the bucket
bucket = client.bucket(bucket_name)

# Make a request to create the bucket
try:
    bucket.create(location='US')  # You can specify the location as needed
    print(f"Bucket {bucket_name} created successfully.")
except Exception as e:
    print(f"Failed to create bucket: {e}")
