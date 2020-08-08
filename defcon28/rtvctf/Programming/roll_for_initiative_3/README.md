## Roll for Initiative 3

### Writeup by Trent (teerix)

Category: Programming

```
The Incident Master got your feedback and fixed his dice. Can you defenders crack it now?

164.90.147.2:1236 
```

There are two changes in this version of the challenge vs the first two. First, you only need to roll the correct number twice
in a row to obtain the flag. Secondly, the roll values this time are actually randomized rather than static. 

As far as I could tell, the randomness was fully random and not based on time. Along with this, with the need for only 2 correct rolls making it
a not-too-bad 1/400 chance to get the right combination, I leaned toward a brute-force implementation using the script below:

```py
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
```

Flag: ts{BHISTheDefendersMustWin}

