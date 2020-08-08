## Warmup

### Writeup by Trent (teerix)

Category: RCE (placed in Pwn folder for simplicity sake)

```
Let's begin with a simple one today.

nc pwnremote.threatsims.com 9000

When you get a shell run 'cat /proc/flag'.

File Included: warmup ELF file
```

This challenge is a rather basic ret2libc attack, but was harder than anticipated for its point value.

Upon running the file, the message `system @ [system() memory address]` is printed, and it asks for input from the user using gets(), so the input can
easily be overflown.

ASLR is enabled, so the `system()` memory address is randomized upon running the binary, but we can use the output message to
our advantage and grab the memory address of `system()` on runtime.

The first thing to figure out using gdb is when eip is overwritten. Running the binary with a padding shows us that it is offset 44 bytes from the stack.

The second thing to find is the location of '/bin/sh', which can be found by the below gdb string:

```
(gdb) find &system,+9999999,"/bin/sh"
0xf7f4d352
warning: Unable to access 16000 bytes of target memory at 0xf7faedda, halting search.
1 pattern found.
(gdb) 
```

With all of this together our payload will be:

`(44 bytes junk) (4 byte system address we grabbed to overwrite eip) (4 bytes junk) (0xf7f4d352 - /bin/sh address)`

I created a script to do just this (included with this writeup), and when I issued `cat /proc/flag`, we get the flag!


Flag: TS{TheObstacleIstheWay}
