#!/user/bin/python3

import socket
import os
import threading
from queue import Queue

# s.settimeout(10)

print_lock = threading.Lock()
#setup host to scan
host = ""
port = 139
global total
total = 0

def gethost():
    hostInput = input("Enter the ipv4 address to scan.\nleave blank for loopback address.\n")
    if(hostInput == "default" or hostInput == "Default" or hostInput == ""):
        print("127.0.0.1 is the ip being scanned \n")
        return "127.0.0.1"
    else:
        print(f"{hostInput} is the ip being scanned \n")
        return hostInput


def portScanner(port):
    # AF_INET specifies we are working with ipv4 addresses
    # SOCK_STREAM specifies type of connection (TCP(handshake))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print(f"trying {port}")        
    global total

    try:
        conn = s.connect((host, port))
        with print_lock:
            print(f'{port}\tOPEN')
                
            total += 1
        conn.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portScanner(worker)
            
        q.task_done()

q = Queue()

host = gethost()

print("Port\tState\n")

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True        
    t.start()

for worker in range(1, 65537):
    q.put(worker)

q.join()

if total == 0:
    print("no ports available")
else:
    print(f"\n{total} ports open.")

while True:
    portNum = input("\ncheck a service via port number.\nType exit to quit.\n")
    if(portNum == 'exit'):
        print("\n\nThanks For using my port scanner.\nCreator: Noel\n\nGoodbye.")
        break
    try:
        serv = socket.getservbyport(int(portNum), 'tcp')
        print(f"\nport {portNum} is running {serv}")
    except:
        print(f"\nport {portNum} service is receiving an error.\nCannot retrieve service the port is listening for.")
    

