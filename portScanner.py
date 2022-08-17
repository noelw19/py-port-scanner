#!/user/bin/python3

import socket
import os

# AF_INET specifies we are working with ipv4 addresses
# SOCK_STREAM specifies type of connection (TCP(handshake))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
#setup host to scan
host = ""
port = 139

def gethost():
    hostInput = input("Enter the ipv4 address to scan.\nleave blank for loopback address.\n")
    if(hostInput == "default" or hostInput == "Default" or hostInput == ""):
        print("127.0.0.1 is the ip being scanned \n")
        return "127.0.0.1"
    else:
        print(f"{hostInput} is the ip being scanned \n")
        return hostInput

def getPort():
    print()
    portInput = input("Enter the port to check.\nleave blank for port 80.\n")
    if(portInput == "default" or portInput == "Default" or portInput == ""):
        print("80 is the port being scanned \n")
        return 80
    else:
        print(f"{portInput} is the port being scanned \n")
        return int(portInput)

def portScanner(port):
    if s.connect_ex((host, port)):
        print('port is closed')
    else:
        print('port is open')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

host = gethost()
port = getPort()

clearConsole()
print(f"scanning ip: {host} \nport: {port}\n")
portScanner(port)
