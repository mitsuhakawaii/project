from pwn import *

r = remote("121.170.91.31", 3333)

DATA = r.recvuntil("add eax, edx")

eax = 0
ebx = 0
ecx = 0
edx = 0
DATA.split('\0')
data = DATA.split('\n')
print data

r.success("Original eax : %s" %str(eax))
r.success("Original ebx : %s" %str(ebx))
r.success("Original ecx : %s" %str(ecx))
r.success("Original edx : %s" %str(edx))

for i in range(6, 16):
	assembly = data[i][0:3]
	r.success("register Assembly : %s" %assembly)
	register = data[i][4:7]
	r.success("register kind : %s" %register)
	number = data[i][9:13]
	r.success("register number : %s" %number)
	if assembly == "add":
		if register == "eax":
			eax += int(number, 0)
		if register == "ebx":
			ebx += int(number, 0)
		if register == "ecx":
			ecx += int(number, 0)
		if register == "edx":
			edx += int(number, 0)
	elif assembly == "sub":
		if register == "eax":
			eax -= int(number, 0)
		if register == "ebx":
			ebx -= int(number, 0)
		if register == "ecx":
			ecx -= int(number, 0)
		if register == "edx":
			ecx -= int(number, 0)
	
eax += ebx
eax += ecx
eax += edx

print eax

print r.recv(1024)
r.sendline(str(eax))

r.interactive()
