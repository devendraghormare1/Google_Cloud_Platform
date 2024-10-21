import requests
import csv

# New API endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Send request to the new API
response = requests.get(url, verify=False)

# Print response content to debug
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")  # This will help debug the issue

# Process the response
if response.status_code == 200:
    try:
        # Get the list of posts
        data = response.json()
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        data = []

    if data:
        # Prepare CSV file to write
        csv_filename = 'posts.csv'
        field_names = ['userId', 'id', 'title', 'body']

        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            
            # Process each post in the response
            for entry in data:
                writer.writerow({
                    'userId': entry.get('userId'),
                    'id': entry.get('id'),
                    'title': entry.get('title'),
                    'body': entry.get('body')
                })

        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the API.")
else:
    print(f"Failed to fetch data: {response.status_code}")
    print(f"Response: {response.text}")
