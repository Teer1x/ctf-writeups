from pwn import *

rolls = []

while True:
	conn = remote('164.90.147.2', 1235)
	conn.recvuntil(b'What did you roll?')


	if len(rolls) != 100:
		for r in rolls:
			conn.send(f'{r}')
			conn.recvuntil(b'Roll again!\n')
			
		conn.send(b'21')
		conn.recvuntil(b'I was looking for was ')
		line = conn.recvline()
		rolls.append(int(line.strip()))
	else:
		for i in range(99):
			conn.send(f'{rolls[i]}')
			conn.recvuntil(b'Roll again!\n')
		conn.send(f'{rolls[99]}')
		flag = conn.recvline().strip()
		print(str(flag, 'utf-8'))
		conn.close()
		break
