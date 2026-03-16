# print("test")

# import requests 

# url = "https://stream.wikimedia.org/v2/stream/recentchange"

# headers = {"User-Agent": "AppleProject/1.0 (github link and email)"}
# response = requests.get(url=url,headers=headers)
# print(response.text)



import requests
import sseclient
import json

# 1. Define the URL of the SSE endpoint
url = 'https://stream.wikimedia.org/v2/stream/recentchange'

# 2. Make the initial request (SSEClient handles the connection)
# The client automatically adds Cache-Control: nocache and Accept: text/event-stream headers [7].
headers = {"User-Agent": "AppleProject/1.0 (github link and email)"}
response = requests.get(url, stream=True,headers=headers)

# 3. Create the SSEClient instance
client = sseclient.SSEClient(response)

print(type(client))
# 4. Iterate over messages as they arrive
print("Listening for Server-Sent Events...")
for msg in client:
    if msg.data:
        try:
            # If data is JSON, parse it
            data = json.loads(msg.data)
            print(f"Received data: {data}")
            # Example: print specific field
            # print(f"Filter Name: {data['FilterName']}")
        except json.JSONDecodeError:
            # Handle non-JSON data
            print(f"Received text: {msg.data}")
    # You can also check msg.event, msg.id, etc.
    # print(f"Event: {msg.event}, ID: {msg.id}")
