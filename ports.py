#!/usr/bin/env python3
import socket
import datetime
import sys


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        # keep track of open ports, open ports in empty list
        self.open_ports = [];

    def __repr__(self):
        return 'Scanner: {}'.format(self.ip)

    def add_port(self, port):
        self.open_ports.append(port)

    #Check to see if port is open
    def scan(self, lowerport, upperport): #Scan a range of ports
        #+1 Included For overrun because the range is not inclusive on the right side
        for port in range(lowerport, upperport + 1):
            #If port is open
            if self.is_open(port):
                #print(port) #print open ports
                #Add the port, From "add_port" definition
                self.add_port(port)

    #Report if port is open, This is using "sockets" import
    def is_open(self, port):
        #create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Putting in result to close the port before the return
        result = s.connect_ex((self.ip, port)) #try to connect and get the error code
        #Close the socket
        s.close()
        # Zero means there was no error code and the socket is open
        return result == 0

    #Output results to file
    def write(self, filepath):
        #Ports return as integer, need them to be interpreted as string via map function
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            # /n To put each finding on it online, otherwise it is one long string
            f.write('\n'.join(openport))


#function that runs the main function
def main():
    ip = input("Enter IP address: ")
    # ip = sys.argv[1]
    scanner = Scanner(ip)
    # Timestamp to use in file name to mark when evidence was hashed
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%I-%M-%S")
    print(repr(scanner)) #prints the ip to be scanned
    scanner.scan(1, 65535)
    print(scanner.open_ports) #Show open ports
    #writing the results to file
    # scanner.write(ip + "_openports_" + timestamp + ".txt")

if __name__ == '__main__':
    main()

# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# result = sock.connect_ex(('127.0.0.1',445))
# if result == 0:
#    print("Port is open")
# else:
#    print("Port is not open")
# sock.close()