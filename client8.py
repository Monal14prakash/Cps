import socket

# Create a socket object
s = socket.socket()

# Define the server's IP and port
port = 12346

# Connect to the server
s.connect(('127.0.0.1', port))

# Receive data from the server and decode it
print(s.recv(1024).decode())

# Close the connection
s.close()
