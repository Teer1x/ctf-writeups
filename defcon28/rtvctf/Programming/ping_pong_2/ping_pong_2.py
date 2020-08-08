from pwn import *

conn = remote('164.90.147.2', 2346)

string = 'T'
conn.recvuntil(b'T')
conn.send(b'T')

while True:
	c = conn.recvline().strip()
	string += str(c, 'utf-8')
	if c == b'}':
		break
	conn.send(c)


conn.close()

print(string)
