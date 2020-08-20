## OverTheWire Leviathan

### Writeup by Trent (teerix)



### Level 5

Contained in the home directory is the binary file `leviathan5`, which according to `ltrace` begins with an fopen on file `/tmp/file.log` and returns an error to the user if it does not exist. If it is created, it will simply read the file character by character until EOF.

As this binary's Owner UID is set to leviathan6, it allows us to view the `/etc/leviathan_pass/leviathan6` as long as we are contained within the binary (like level 2), so we have to figure out a way to read in `/tmp/file.log` in a way that calls the password file; symbolic linkage works well for this!

```sh
leviathan5@leviathan:~$ ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
leviathan5@leviathan:~$ ./leviathan5 
UgaoFee4li
leviathan5@leviathan:~$ 
```

Level 6 Password: UgaoFee4li



### Level 6

Contained in the home directory is binary file `leviathan6`, which asks for a 4-digit number as an arg and either gives you a shell, or returns "Wrong". Unlike other challenges similar to this, this is not done by a strcmp() and therefore is not seen in the `ltrace`.

Opening up the binary in gdb and disassembling main shows this:

```
...
0x08048587 <+76>:    call   0x8048420 <atoi@plt>
0x0804858c <+81>:    add    $0x10,%esp
0x0804858f <+84>:    cmp    -0xc(%ebp),%eax
0x08048592 <+87>:    jne    0x80485bf <main+132>
...
```

Which shows that the binary takes your given 4 digits, converts to an int, and compares it to the value 0xC bytes before the base pointer, `ebp`.

I set a breakpoint at the comparison, ran it with a random 4-digit value and examined the value at -0xC(%ebp).

```
(gdb) x/d $ebp-0xc
0xffffd69c:     7123
```

As shown above, 7123 was contained at that memory location.

Rerunning the binary with 7123 gives you a shell as leviathan7, simply `cat /etc/leviathan_pass/leviathan7` for the password!

Note: Since the possible values are 0000-9999, it is very easy to just brute force this challenge with a script, but this was a bit more sophisticated method of achieving the same thing!

Level 7 Password: ahy7MaeBo9