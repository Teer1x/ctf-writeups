## Ping Pong

### Writeup by Trent (teerix)

Category: Programming

```
Would you like to play a game?

A game of Ping Pong?

164.90.147.2:2345 
``

Connecting to the challenge gives an ASCII ping pong screen with a single character at the bottom ('T' at the start). Typing
this letter and hitting enter pops up a difference character. Doing this a few times shows that it is slowly printing the string
character by character. You could technically do this manually, but I created a script to automatically grab the characters.

```py
from pwn import *

conn = remote('164.90.147.2', 2345)

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

The string the challenge gives is: TheFlagforthischallengeis:ts{IreallymissThePongs}

Flag: ts{IreallymissThePongs}
