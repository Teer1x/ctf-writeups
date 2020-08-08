## Ping Ping 2

### Writeup by Trent (teerix)

Category: Programming

```
I see you like this game, can you play fast?

164.90.147.2:2346 
```

My prior script to the first Ping Pong challenge is fast enough to work here as well, so I simply used the same script, modifying the port!

```py
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
```

Flag: ts{YouGottaGetQuickToScoreTheFlag}
