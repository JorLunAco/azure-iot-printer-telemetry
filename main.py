import os
from azure.iot.device import IoTHubDeviceClient, Message
import json, random, time

CONNECTION_STRING = os.getenv("AZURE_IOT_HUB_CONNECTION_STRING")
if not CONNECTION_STRING:
    raise ValueError("AZURE_IOT_HUB_CONNECTION_STRING env var not set")

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

while True:
    payload = {
        "nozzle_temp_c": round(random.uniform(195, 215), 1),
        "bed_temp_c": round(random.uniform(58, 62), 1),
        "layer": random.randint(0, 500),
        "status": random.choice(["printing", "idle", "error"])
    }
    
    client.send_message(Message(json.dumps(payload)))
    print("sent:", payload)
    time.sleep(5)
    