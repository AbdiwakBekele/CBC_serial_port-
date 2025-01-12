import serial
import requests

port = 'COM7'
baudrate = 115200
api_url = 'http://127.0.0.1:8000/api/mindray-receive-data'

# Open the port
with serial.Serial(port, baudrate, timeout=1) as ser:
    print(f"Listening on {port}")
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            received_data = ser.readline().decode('utf-8').strip()
            print(f"Received: {received_data}")

             # Send the data to the Laravel API
            try:
                response = requests.post(api_url, json={'data': received_data})
                if response.status_code == 201:
                    print("Data sent and saved successfully!")
                else:
                    print(f"Failed to send data: {response.status_code}, {response.text}")
            except Exception as e:
                print(f"Error sending data: {e}")