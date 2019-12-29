# The socket package is the standard package to work with communication
# It is easily used to create a socket server and client in the following manner
# Lets start with the server which will act up as an echo server
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print("Starting up on %s port %s" % server_address)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection")
    # Will return the connection socket and the client info as a tuple
    connection, client_address = sock.accept()
    try:
        print("Connection from", client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print("Received '%s'" % data)
            if data:
                print("Sending data back to the client")
                connection.sendall(data)
            else:
                print("no more data from", client_address)
                break
    # Note that we are using finally while completely ignoring an exception
    # This will always happen no matter what
    finally:
        # Clean up the connection
        connection.close()

# The echo client is also pretty simple and is implemented in the following
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print("Connecting to %s port %s" % server_address)
sock.connect(server_address)
try:
    # Send data
    message = 'This is a repeated message.'
    print("Sending '%s'" % message)
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("Received '%s'" % data)
finally:
    print('Closing socket')
    sock.close()