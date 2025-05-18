import socket
import termcolor

def scan(targets, ports):
    for port in range (1, ports):
        scan_port(targets,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print('Port Opened ' + str(port))
        sock.close()
    except:
        pass
 
targets = input("Enter Target to Scan: ")
ports =  int(input("Enter How Many Ports to Scan: "))
scan(targets, ports)