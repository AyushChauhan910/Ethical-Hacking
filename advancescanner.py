#!/usr/bin/python

from socket import *
import optparse
from threading import *

def portScan(tgtHost,tgtPorts):
        try:
                tgtIP = gethostbyname(tgtHost)
        except:
                print("Unknown Host - %d" % tgtHost)

        try:
                tgtName = gethostbyaddr(tgtIP)
                print("[+] Scan results for : " + tgtName)
        except:
                print("[+] Scan results for : " + tgtIP)

        setdefaulttimeout(1)

        for tgtPort in tgtPorts:
                t = Thread(target = connScan , args = (tgtHost , int(tgtPort)))
                t.start()


def main():
        parser = optparse.OptionParser('Usage of program : ' + '-H <targest host>  -p <target port>')
        parser.add_option('-H' , dest = 'tgtHost' , type = 'string' , help = 'specify target host')
        parser.add_option('-p' , dest = 'tgtPort' , type = 'string' , help = 'specify number of ports seperated by comma')
        (options , args) = parser.parse_args()
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')
        if (tgtHost == None) | (tgtPorts[0]==None):
                print(parser.usage)
                exit(0)
        portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
        main()
