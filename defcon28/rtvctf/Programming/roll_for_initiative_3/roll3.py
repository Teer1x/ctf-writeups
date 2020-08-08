from pwn import *
import random

while True:
	conn = remote('164.90.147.2', 1236)
	conn.recvuntil(b'What did you roll?\n')


	conn.send(f'{random.randrange(1, 21)}')

	line = conn.recvline()

	if line == b'Correct\n':
		conn.recvline()
		conn.send(f'{random.randrange(1,21)}')

		flag = str(conn.recvline(), 'utf-8')
		if 'Sorry' in flag:
			print("Sorry in flag")
		else:
			print(flag)
			break
	else:
		conn.close()
