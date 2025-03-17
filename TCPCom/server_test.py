import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address (host, port)
server_socket.bind(('0.0.0.0', 12345))  # '0.0.0.0' means listen on all available interfaces

# Listen for incoming connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept the connection
connection, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Open a file to save the received data
with open('received_data.txt', 'wb') as file:
    try:
        while True:
            # Initialize an empty variable to accumulate the data
            data = b''
            
            # Receive data in 5 MB chunks
            while True:
                chunk = connection.recv(5 * 1024 * 1024)  # 5 MB buffer size
                data += chunk
                if len(chunk) < (5 * 1024 * 1024):
                    break
            
            # If data is received, write it to the file
            if data:
                file.write(data)
                print(f"Received and saved data: {data.decode('utf-8', errors='ignore')}")
            else:
                break
    finally:
        # Clean up the connection
        connection.close()

print("Data has been saved to 'received_data.txt'")
