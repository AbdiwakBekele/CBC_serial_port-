import socket
import re

def parse_cbc_parameters(data):
    """
    Extract CBC parameters from HL7-like data format.
    """
    cbc_parameters = {}
    cbc_patterns = {
        "WBC": r"OBX\|\d+\|NM\|6690-2\^WBC\^LN\|\|([\d.]+)\|10\^9/L",
        "Lymph#": r"OBX\|\d+\|NM\|731-0\^Lymph#\^LN\|\|([\d.]+)\|10\^9/L",
        "Mid#": r"OBX\|\d+\|NM\|10027\^Mid#\^99MRC\|\|([\d.]+)\|10\^9/L",
        "Gran#": r"OBX\|\d+\|NM\|10028\^Gran#\^99MRC\|\|([\d.]+)\|10\^9/L",
        "Lymph%": r"OBX\|\d+\|NM\|736-9\^Lymph%\^LN\|\|([\d.]+)\|%",
        "Mid%": r"OBX\|\d+\|NM\|10029\^Mid%\^99MRC\|\|([\d.]+)\|%",
        "Gran%": r"OBX\|\d+\|NM\|10030\^Gran%\^99MRC\|\|([\d.]+)\|%",
        "RBC": r"OBX\|\d+\|NM\|789-8\^RBC\^LN\|\|([\d.]+)\|10\^12/L",
        "HGB": r"OBX\|\d+\|NM\|718-7\^HGB\^LN\|\|([\d.]+)\|g/dL",
        "HCT": r"OBX\|\d+\|NM\|4544-3\^HCT\^LN\|\|([\d.]+)\|%",
        "MCV": r"OBX\|\d+\|NM\|787-2\^MCV\^LN\|\|([\d.]+)\|fL",
        "MCH": r"OBX\|\d+\|NM\|785-6\^MCH\^LN\|\|([\d.]+)\|pg",
        "MCHC": r"OBX\|\d+\|NM\|786-4\^MCHC\^LN\|\|([\d.]+)\|g/dL",
        "RDW-CV": r"OBX\|\d+\|NM\|788-0\^RDW-CV\^LN\|\|([\d.]+)\|%",
        "RDW-SD": r"OBX\|\d+\|NM\|21000-5\^RDW-SD\^LN\|\|([\d.]+)\|fL",
        "PLT": r"OBX\|\d+\|NM\|777-3\^PLT\^LN\|\|([\d.]+)\|10\^9/L",
        "MPV": r"OBX\|\d+\|NM\|32623-1\^MPV\^LN\|\|([\d.]+)\|fL",
        "PDW" : r"OBX\|\d+\|NM\|32207-3\^PDW\^LN\|\|([\d.]+)\|\|[\d.]+-[\d.]+",
        "PCT":  r"OBX\|\d+\|NM\|10002\^PCT\^99MRC\|\|([\d.]+)\|\%",
        "P-LCC": r"OBX\|\d+\|NM\|10013\^P-LCC\^99MRC\|\|([\d.]+)\|10\^9/L",
        "P-LCR": r"OBX\|\d+\|NM\|10014\^P-LCR\^99MRC\|\|([\d.]+)\|\%"
    }

    for param, pattern in cbc_patterns.items():
        match = re.search(pattern, data)
        if match:
            cbc_parameters[param] = match.group(1)

    return cbc_parameters

# TCP server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5800))  # Bind to all interfaces on port 5800
server_socket.listen(1)
print("Server is waiting for a connection...5800")

while True:
    # Accept a connection
    connection, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        # Receive the data in chunks
        data_buffer = b""
        while True:
            data = connection.recv(8 * 1024)  # Receive up to 8 KB
            if data:
                data_buffer += data

                # Decode and process the data
                data_str = data_buffer
                print(f"Received raw data:\n{data_str}")

                # Extract CBC parameters
                #cbc_results = parse_cbc_parameters(data_str)
                # print("\nExtracted CBC Parameters:")
                # for param, value in cbc_results.items():
                #     print(f"{param}: {value}")

            else:
                break

       

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up the connection
        connection.close()
        print("Connection closed.")
