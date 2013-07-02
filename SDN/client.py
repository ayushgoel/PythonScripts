#! /usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 45341

s.connect((host, port))
print "Client running..."
for i in xrange(50):
  s.sendall("Sending " + str(i))
  print s.recv(1024)
s.close()
