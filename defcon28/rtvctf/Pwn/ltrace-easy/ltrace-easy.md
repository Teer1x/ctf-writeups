## ltrace-easy

### Writeup by Trent (teerix)

Category: Pwn

```
Can you run the binary?

You may have to trace it or something.

File Included: ltrace-easy ELF file
```

When run normally, the binary does not produce any output.

When run using ltrace, the first strcmp the program does is check your current username to "mark". This requires you to create
an account named mark using `adduser`/`useradd`.

The second comparison is the program compares your current working directory against `/home/mark/development/game`.

To pass this, change to the "mark" user (`su mark`) and create the directory path `development/game`.

The last comparison is checking to see if `/tmp/marksgame.log` file is available to write to.

To pass this, just issue `touch /tmp/marksgame.log`

When all of this is done, the ltrace shows the `putchar()` call, which displays the flag.

Flag: ts{whydidyouevenrunit}
