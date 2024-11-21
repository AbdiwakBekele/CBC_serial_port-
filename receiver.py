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




# import serial
# import mysql.connector

# # Configure database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="hospital_db"
# )
# cursor = db.cursor()

# # Configure COM2
# port = 'COM2'
# baudrate = 9600

# with serial.Serial(port, baudrate, timeout=1) as ser:
#     print(f"Listening on {port}")
#     while True:
#         if ser.in_waiting > 0:  # Check if data is available
#             received_data = ser.readline().decode('utf-8').strip()
#             print(f"Received: {received_data}")
            
#             # Parse data
#             data_parts = received_data.split(';')
#             parsed_data = {kv.split(':')[0]: kv.split(':')[1] for kv in data_parts if ':' in kv}

#             # Insert into database
#             query = """
#                 INSERT INTO cbc_results (SampleID, WBC, RBC, HGB, HCT)
#                 VALUES (%s, %s, %s, %s, %s)
#             """
#             values = (
#                 parsed_data.get("SampleID"),
#                 parsed_data.get("WBC"),
#                 parsed_data.get("RBC"),
#                 parsed_data.get("HGB"),
#                 parsed_data.get("HCT"),
#             )
#             cursor.execute(query, values)
#             db.commit()
#             print("Data saved to database.")
