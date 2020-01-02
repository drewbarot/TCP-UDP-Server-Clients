'''
Dhrumil Barot
250970442
CS3357
Assn 2

This file is a UDP client. 

'''

# Library imports
import socket
import time

# Set local address IP and use a standard port.
udp_ip = '127.0.0.1'
udp_port = 8080

# Give client information about connection
print("Attempting to contact server at ", udp_ip, ":", udp_port)

# Create socket and connect
sock_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect and ask for input
# Should be "What is the current date and time?"
message = input("Please enter a message for the server: ")  
sock_conn.sendto(message.encode(), (udp_ip, udp_port))

# Accept server response and print response. Sleep so you can actually read it.
data, server = sock_conn.recvfrom(1024)
print(data.decode())
time.sleep(3)

# Terminate connection
sock_conn.close()
