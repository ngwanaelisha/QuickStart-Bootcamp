#!usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call("exit 1", shell=True)

# Ask for input
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServer)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scan all ports)
# We also put ins some error handling for catching errors

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:    Open".format(port))
        sock.close()

except socket.gaierror:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run
total = t2 - t1

# Printing the information to screen
print("Scanning Complete in: ", total)

print("Start time: ", t1)
print("End time: ", t2)
