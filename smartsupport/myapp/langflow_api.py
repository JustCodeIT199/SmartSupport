import os
import requests

# Replace with your actual API endpoint URL
url = "https://api.langflow.astra.datastax.com/lf/7c02a9dd-01b9-48a9-9956-57c2db1b976e/api/v1/run/9f8e9ff4-1b23-498a-8252-aa8b84caa857"

# Request payload configuration
payload = {
    "input_value": "hi",  # The input value to be processed by the flow
    "output_type": "chat",  # Specifies the expected output format
    "input_type": "chat"  # Specifies the input format
}

# Retrieve the application token from an environment variable
application_token = os.getenv("AstraCS:kMuJzZHusbphuPrZHZraXjjG:1c8623ed51ccb531cdc9a63acefd70e13e6e10ea5170b0bb6dc997f88cac93d4")

if not application_token:
    raise ValueError("Application token not found. Set the 'APPLICATION_TOKEN' environment variable.")

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {application_token}"  # Use the token from the environment variable
}

try:
    # Send API request
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for HTTP errors

    # Parse and print the JSON response
    response_data = response.json()
    print("Response:", response_data)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")