import time
import random
import os
from azure.iot.device import IoTHubDeviceClient, Message
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

CONNECTION_STRING = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING_FIFTH_AVENUE")

def get_telemetry():
    return {
        "location": "Fifth Avenue",
        "iceThickness": round(random.uniform(20.0, 40.0), 2),
        "surfaceTemperature": round(random.uniform(-15.0, 2.0), 2),
        "snowAccumulation": round(random.uniform(0.0, 20.0), 2),
        "externalTemperature": round(random.uniform(-20.0, 5.0), 2)
    }

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending telemetry to IoT Hub...")
    try:
        while True:
            telemetry = get_telemetry()
            message = Message(str(telemetry))
            client.send_message(message)
            print(f"Sent message: {message}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()