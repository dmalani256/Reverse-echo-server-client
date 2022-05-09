# import the socket library
import socket

# create a socket object using the built-in function of AF_INET and SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reserve a port
port = 5050

# connect to the server on local computer
s.connect(('localhost', port))

# create while loop until we interrupt it or an error occurs
while True:
    # input the data you want to send to the sever and send it encoded
    input_string = input("Enter data you want to send-> ")
    s.send(input_string.encode())

    # message will be sent back from the server decoded and printed out
    message = s.recv(1024).decode()
    print("Entered data-> ", message)
    print()

    # now if the message is equivalent to "dne" or if the client inputs "end", then the loop will stop
    if message == "dne":
        break
