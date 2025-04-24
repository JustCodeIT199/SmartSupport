
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/7c02a9dd-01b9-48a9-9956-57c2db1b976e/api/v1/run/9f8e9ff4-1b23-498a-8252-aa8b84caa857"  

# Request payload configuration
payload = {
    "input_value": "hi ",  # The input value to be processed by the flow
    "output_type": "chat",  # Specifies the expected output format
    "input_type": "chat"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <AstraCS:kMuJzZHusbphuPrZHZraXjjG:1c8623ed51ccb531cdc9a63acefd70e13e6e10ea5170b0bb6dc997f88cac93d4>"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    