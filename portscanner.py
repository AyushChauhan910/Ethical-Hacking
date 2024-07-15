#!/usr/bin/python
import socket

sock =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("Enter IP address : ")

port =int(input("Enter port: "))

def portscanner(port):
        if sock.connect_ex((host,port)):
                print("Port {} is closed".format(port))
        else:
                print("Port %d is open" % (port))

portscanner(port)
