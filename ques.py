# ## Scenario
# * You're tasked with building a real-time pipeline that monitors Wikipedia page edits to identify trending topics and user activity patterns.
 
# ### Part 1: Project Setup  
 
# * Set up a basic Python project (or language of your choice)
 
# ### Part 2: Data Ingestion  
 
# * Stream Source: Wikipedia's real-time recent changes stream
 
# * Endpoint: https://stream.wikimedia.org/v2/stream/recentchange  
 
# * Format: Server-sent events (SSE) with JSON payloads
 
# ### Tasks:
 
# - Write code to connect to and consume the Wikipedia changes stream (use sseclient-py, or equivalent for your chosen language)
 
# - Parse the incoming JSON events
 
# - Filter out the following events (edits from bots, zero length edits)
 
# - Key fields to capture: timestamp, user, title, comment, length_change, wiki 



print("test")
import json
import pprint
import sseclient



def with_requests(url, headers):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True, headers=headers)


url = 'https://stream.wikimedia.org/v2/stream/recentchange'
headers = {'Accept': 'text/event-stream',"User-Agent": "AppleProject/1.0 (github link and email)"}
response = with_requests(url, headers)  # or with_requests(url, headers)
client = sseclient.SSEClient(response)
for event in client.events():
    val = json.loads(event.data)
    if (val['bot']) :
        pprint.pprint(val.get('length', 'No length field'))