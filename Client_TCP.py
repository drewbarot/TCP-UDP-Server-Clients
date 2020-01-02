'''
Dhrumil Barot
250970442
CS3357
Assn 2

This file is a TCP client. 

'''
# Library imports
import socket
import time

# Set local address IP and use a standard port.
tcp_ip = '127.0.0.1'
tcp_port = 8080

# Give client information about connection
print("Attempting to contact server at ", tcp_ip, ":", tcp_port)

# Create socket and connect
sock_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_conn.connect((tcp_ip, tcp_port))

# Connect and ask for input
print("Connection to server established...")
# Should be "What is the current date and time?"
message = input("Please enter a message for the server: ")  

# Send the message to the server
sock_conn.sendall(message.encode())

# Accept server response and print response. Sleep so you can actually read it.
data = sock_conn.recv(1024)
print(data.decode())
time.sleep(3)


# Terminate connection
sock_conn.close()
