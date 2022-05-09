# import the socket library
import socket

# create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port and IP address on your computer by using the built-in function gethostname()
port = 5050
IP = socket.gethostname()

# bind the port and print the IP address and port number
s.bind(('', port))
print("socket binded to " + IP + " on port " + str(port))

# put the socket into listening mode
s.listen(999)
print("socket is listening")

# accept the incoming connection from client
c, address = s.accept()
print("New Connection made!")

# create while loop until we interrupt it or an error occurs
while True:

    # Get data from client that is decoded and print it
    msg = c.recv(1024).decode()
    print("Message Input: ", msg)

    # Reverse the data received from client, print it, and send back to the client encoded
    message = msg[::-1]
    print("Message Output: ", message)
    print()
    c.send(message.encode())

    # now if the message is equivalent to "dne" or if the client inputs "end", then the loop will stop
    if message == "dne":
        break