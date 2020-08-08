## Roll for Initiative 2

### Writeup by Trent (teerix)

Category: Programming

```
You thought that was fun? The Incident Master has something else up his sleeve?

164.90.147.2:1235 
```

The only difference to this challenge and the first version is that instead of requiring 10 winning rolls in a row, it requires 100, making it harder to do manually.

I used my script from the first version of the challenge, only slightly modified to find the winning 100 numbers rather than 10.

```py
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
```

Flag: ts{BHISStillWaitingOnMyExpansionPacktobedelivered}
