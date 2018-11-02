"""

This program is made for educational purpose,
this program is just print your Ipv4 addr,
Next Version is will be "find and print ipv4 addr from other network hosts."; (network finder)

And, This is new version of "ipv4 exporter".
this script support function and this file can use independent.

This Progrma is made By Nicht. Lee Joon Sung

(C) 2018 copyright by nicht, Kbu 1822021

"""

# import major libs
import socket

def ipv4_finder():
    host_name = socket.gethostname()
    ip_addr = socket.gethostbyname(host_name)
    print "Host name : %s" %host_name
    print "IP address is : %s" %ip_addr


if __name__ == '__main__':
    print ipv4_finder()
