#!/usr/bin/python
import socket
from termcolor import colored


sock =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("Enter IP address : ")
total_ports = int(input("Enter the number of ports you want to scan: "))


def portscanner(port):
        if sock.connect_ex((host,port)):
                print(colored("Port {} is closed".format(port) , 'red'))
        else:
                print(colored("Port %d is open" % (port) , 'green'))


for port in range(1,total_ports+1):
        portscanner(port)
