#! /usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 45341
s.bind((host, port))

s.listen(5)

print "Server started... port : ", port

while True:
  c, addr = s.accept()
  print "Got connection from ", c, addr
  c.send("Thank you for connecting")
  while True:
    data = c.recv(1024)
    print data
    if not data: break
    c.send("Recieved :" + str(data))
  c.close()
