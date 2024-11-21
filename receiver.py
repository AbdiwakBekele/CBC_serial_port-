import serial

# Configure COM2
port = 'COM7'
baudrate = 9600

# Open the port
with serial.Serial(port, baudrate, timeout=1) as ser:
    print(f"Listening on {port}")
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            received_data = ser.readline().decode('utf-8').strip()
            print(f"Received: {received_data}")
