import re
import socket
import requests
import json

# Function to parse the HL7 message
def parse_hl7(hl7_message):
    segments = hl7_message.split('\r')  # Split the message by segment
    parsed_message = {}

    patient_name = None

    for segment in segments:
        fields = segment.split('|')
        segment_name = fields[0]
        
        # Extract patient name from PID segment
        if segment_name == 'PID':
            patient_name = fields[5]  # Patient name is at index 5
            # We only want the part before the '^' (FirstName^LastName)
            if patient_name:
                patient_name = patient_name.split('^')[1] + " " + patient_name.split('^')[0]

        # Handle only OBX segments (the CBC test results)
        if segment_name == 'OBX':
            test_id = fields[3]
            value = fields[5] if len(fields) > 5 else None
            if test_id and value:
                # Extract only the name of the test (split by '^')
                test_name = test_id.split('^')[1]  # The second part is the test name
                parsed_message[test_name] = value
    
    return patient_name, parsed_message
    
    
# TCP server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 5800))
server_socket.listen(1)
print("Server is waiting for a connection on port 5800...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"\n[INFO] Connection established from {addr}")

    try:
        # Receive data from the machine
        data = client_socket.recv(16 * 1024)
        if not data:
            print("[ERROR] No data received. Closing connection.")
            client_socket.close()
            continue

        # Decode the byte string into a regular string
        data_str = data.decode('utf-8', errors='ignore')
        print(f"[INFO] Received raw data:\n{data_str}")

        # Parse the HL7 message
        patient_name, parsed_data = parse_hl7(hl7_message_str)
        
        # Convert the parsed data into JSON format
        json_data = json.dumps(parsed_data, indent=4)
        print(json_data)

        if not json_data:
            print("[ERROR] No valid CBC parameters extracted. Possible data format mismatch.")
        else:
            print(f"[INFO] Extracted CBC Parameters:\n{json_data}")

            # Prepare data for sending to Laravel API
            api_url = 'http://192.168.100.254/api/genru-receive-data'
            payload = {
                "data": {
                    "patient_name": patient_name,
                    **json_data  # Merge CBC results into the payload
                }
            }
            
            headers = {'Content-Type': 'application/json'}

            try:
                response = requests.post(api_url, json=payload, headers=headers)
                
                print(f"[INFO] Response Status: {response.status_code}")
                if response.status_code == 201:
                    print("[SUCCESS] Data sent and saved successfully!")
                else:
                    print(f"[ERROR] Failed to send data: {response.status_code}, Response: {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"[ERROR] API request failed: {e}")

    except Exception as e:
        print(f"[ERROR] Exception occurred: {e}")

    finally:
        client_socket.close()
        print("[INFO] Connection closed.\n")
	