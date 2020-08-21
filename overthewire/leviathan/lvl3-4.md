## OverTheWire Leviathan

### Writeup by Trent (teerix)



### Level 3

The home directory contains a `level3` binary that when ltraced shows that whatever input password you put in is compared to the string "snlprintf". This is almost the same as level 1's challenge.

```sh
leviathan3@leviathan:~$ ./level3
Enter the password> snlprintf
[You\'ve got shell]!
$ whoami
leviathan4
$ cat /etc/leviathan_pass/leviathan4
vuH0coox6m
```


Level 4 Password: vuH0coox6m



### Level 4

Issuing `ls -al` at the home directory shows a hidden `.trash` directory with a file `bin` contained within.

Executing this file prints out `01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010`.

Converting binary to ASCII, this translates to Tith4cokei, which is the password for level 5.

Level 5 Password: Tith4cokei