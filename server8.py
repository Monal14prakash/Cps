import socket

# Create a socket object
s = socket.socket()

# Define port to bind to
port = 12346

# Bind the socket to the address and port
s.bind(('0.0.0.0', port))  # You can use '' or '0.0.0.0' to bind to all interfaces

# Print success message
print("Socket binded to %s" % (port))

# Start listening for incoming connections
s.listen(5)
print("Server is ready to accept connections")

while True:
    # Accept a connection from a client
    c, addr = s.accept()
    print("Got connection from", addr)

    # Send a message to the client
    c.send('Thanks for connecting'.encode())

    # Close the client connection
    c.close()

    # Optional: You can break here if you want the server to accept only one connection
    # break  # If you want to stop after the first connection, keep this line. Otherwise, remove it.
