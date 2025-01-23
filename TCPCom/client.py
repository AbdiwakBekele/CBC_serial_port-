import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (use the server's IP address and the port used by the server)
server_ip = '192.168.1.2'  # Replace with the actual server IP address
server_port = 5800

client_socket.connect((server_ip, server_port))

# Send data
message = "\x00\x00\x05\xc3\x0bMSH|^~\\&|Genrui|KT-6300|||20250114143247||ORU^R01|10579|P|2.3.1|||||CHA|UTF-8|||\rPID|1||559||HERMELA|||O|||||||||||||||||||||||\rPV1|1|0||||||||||||||||||||\rOBR|1||||||20250114101445|||||||||||LAB||||||HM||||||||Genrui||||||||\rOBX|1|NM|^WBC^||6.44|10^3/uL|4.00-10.00||||F||||||||\rOBX|2|NM|^Lym#^||0.86|10^3/uL|0.80-4.00||||F||||||||\rOBX|3|NM|^Mid#^||0.46|10^3/uL|0.10-1.80||||F||||||||\rOBX|4|NM|^Gran#^||5.12|10^3/uL|2.00-7.80||||F||||||||\rOBX|5|NM|^Lym%^||13.3|%|20.0-40.0|L|||F||||||||\rOBX|6|NM|^Mid%^||7.1|%|1.0-15.0||||F||||||||\rOBX|7|NM|^Gran%^||79.6|%|50.0-75.0|H|||F||||||||\rOBX|8|NM|^RBC^||4.62|10^6/uL|3.50-5.50||||F||||||||\rOBX|9|NM|^HGB^||15.0|g/dL|11.0-18.0||||F||||||||\rOBX|10|NM|^HCT^||43.6|%|37.0-54.0||||F||||||||\rOBX|11|NM|^MCV^||94.4|fL|80.0-100.0||||F||||||||\rOBX|12|NM|^MCH^||32.4|pg|27.0-36.0||||F||||||||\rOBX|13|NM|^MCHC^||34.4|g/dL|32.0-38.0||||F||||||||\rOBX|14|NM|^RDW-CV^||13.3|%|11.0-19.0||||F||||||||\rOBX|15|NM|^RDW-SD^||45.9|fL|35.0-58.0||||F||||||||\rOBX|16|NM|^PLT^||240|10^3/uL|150-450||||F||||||||\rOBX|17|NM|^MPV^||9.1|fL|7.0-14.0||||F||||||||\rOBX|18|NM|^PDW-CV^||13.6|%|15.0-19.0|L|||F||||||||\rOBX|19|NM|^PDW-SD^||12.9|fL|9.0-19.0||||F||||||||\rOBX|20|NM|^PCT^||0.219|%|0.108-0.300||||F||||||||\rOBX|21|NM|^P-LCR^||23.0|%|11.0-49.0||||F||||||||\rOBX|22|IS|^Take Mode^||O||||||F||||||||\rOBX|23|IS|^Blood Mode^||WH||||||F||||||||\rOBX|24|IS|^Ref Group^||General||||||F||||||||\rOBX|25|IS|^Age^||||||||F||||||||\rOBX|26|IS|^Remarks^||||||||F||||||||\r\x1c\r"
client_socket.sendall(message.encode('utf-8'))

# Close the connection
client_socket.close()
