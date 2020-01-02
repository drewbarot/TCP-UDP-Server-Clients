'''
Dhrumil Barot
250970442
CS3357
Assn 2

This file is a UDP server. 

'''

# Library imports
from datetime import datetime
import socket

# Set local address IP and use a standard port.
udp_ip = '127.0.0.1'
udp_port = 8080

# Create the socket connection from the socket library, then bind it to the above variables
sock_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_conn.bind((udp_ip, udp_port))
on = True
print("Connected. Listening...")

# While the server is listening...
while(on):
    msg, addr = sock_conn.recvfrom(1024)
    # Accept one very specific case for the client to ask what the current date/time is and respond 
    if msg.decode() == "What is the current date and time?":
        reply = "Current Date and Time – " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        sock_conn.sendto(reply.encode(), addr)
    # Allow the user to disconnect
    elif msg.decode() == "end":
        response = "The server was closed. "
        sock_conn.sendto(response.encode(), addr)
        on = False
    # If there's a problem, send an error message
    else:
        response = "The message was invalid. "
        sock_conn.sendto(response.encode(),addr)

# Terminate connection and close. 
sock_conn.close()
