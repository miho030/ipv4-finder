"""

This program is made for educational purpose,
this program is just print your Ipv4 addr,
Next Version is will be "find and print ipv4 addr from other network hosts."; (network finder)

This Progrma is made By Nicht. Lee Joon Sung

(C) 2018 copyright by nicht, Kbu 1822021

"""

import socket

# call gethostname() method and insert variable data at host_name
host_name = socket.gethostname()

# print my hostname
print "Host name : %s" %host_name

print "IP address : %s" %socket.gethostbyname(host_name)
