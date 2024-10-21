from google.oauth2 import service_account
from googleapiclient.discovery import build
import time

# Define your project, zone, and VM settings
project_id = "learning-gcp-cyb"    # Replace with your GCP project ID
zone = "us-central1-a"            # Replace with the desired zone
instance_name = "my-vm-instance"  # The name for your VM instance
machine_type = "e2-micro"    # Machine type (e.g., n1-standard-1)
image_family = "debian-11"        # OS image family (Debian in this case)
image_project = "debian-cloud"    # Image project ('debian-cloud' for Debian)

# Path to your service account key file
key_path = "E:/workspace/GCP/compute_operations/key.json"   # Replace with the path to your key.json file

# Load credentials from the service account key file
credentials = service_account.Credentials.from_service_account_file(key_path)

# Build the Compute Engine service
compute = build('compute', 'v1', credentials=credentials)

# Get the latest image from the specified image family
def get_latest_image(compute, project, family):
    response = compute.images().getFromFamily(project=project, family=family).execute()
    return response['selfLink']

# Function to create a VM instance
def create_instance(compute, project, zone, name, machine_type, image_link):
    config = {
        "name": name,
        "machineType": f"zones/{zone}/machineTypes/{machine_type}",
        "disks": [
            {
                "boot": True,
                "autoDelete": True,
                "initializeParams": {
                    "sourceImage": image_link,
                },
            },
        ],
        "networkInterfaces": [
            {
                "network": "global/networks/default",  # Using the default network
                "accessConfigs": [
                    {
                        "type": "ONE_TO_ONE_NAT",
                        "name": "External NAT",
                    }
                ],
            }
        ],
    }

    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config
    ).execute()

# Get the latest Debian image link
image_link = get_latest_image(compute, image_project, image_family)

# Create the VM instance
print(f"Creating VM instance '{instance_name}'...")
operation = create_instance(compute, project_id, zone, instance_name, machine_type, image_link)

# Wait for the operation to complete
def wait_for_operation(compute, project, zone, operation):
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation['name']).execute()

        if result['status'] == 'DONE':
            print("VM creation complete.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(5)

# Wait for the VM creation to finish
wait_for_operation(compute, project_id, zone, operation)

print(f"VM instance '{instance_name}' created successfully.")
