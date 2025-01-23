import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (use the server's IP address and the port used by the server)
server_ip = '192.168.1.100'  # Replace with the actual server IP address
server_port = 12345

client_socket.connect((server_ip, server_port))

# Send data
message = "Hello from the client!"
client_socket.sendall(message)

# Close the connection
client_socket.close()
