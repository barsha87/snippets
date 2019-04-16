import sys
import telnetlib
HOST = '10.126.94.50'
user = 'admin'
password = 'nbv_12345'

tn = telnetlib.Telnet(HOST, 23, 5) #5 is timeout value
tn.write("login\r\n")
tn.write(user+ "\r\n")
tn.write(password+ "\r\n")
tn.write("rb 3\r\n") #this reboots plug 3
tn.write("rb 1\r\n") #this reboots plug 1
tn.write("logout\r\n")
tn.close
