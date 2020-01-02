'''
Dhrumil Barot
250970442
CS3357
Assn 2

This file is a TCP server. 

'''

# Library imports
from datetime import datetime
import socket

# Set local address IP and use a standard port. 
tcp_ip = '127.0.0.1'
tcp_port = 8080

# Create the socket connection from the socket library, then bind it to the above variables
sock_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_conn.bind((tcp_ip, tcp_port))

# Start listening
sock_conn.listen(1)
print("Connected. Listening...")

on = True

# While the server is listening...
while(on):    
    conn, addr = sock_conn.accept()
    sock_conn.listen(1)
    data = conn.recv(1024)
    # Accept one very specific case for the client to ask what the current date/time is and respond 
    if data.decode() == "What is the current date and time?":
        reply = "Current Date and Time – " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        conn.send(reply.encode())
    # Allow the user to disconnect
    elif data.decode() == "end":
        reply = "The server was closed. "                         
        conn.send(reply.encode())
        on = False
    # If there's a problem, send an error message
    else:
        reply = "The message was invalid. "
        conn.send(reply.encode())

# Terminate connection and close. 
print("Shutting down server...")
sock_conn.close()
