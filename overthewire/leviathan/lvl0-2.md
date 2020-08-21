## OverTheWire Leviathan

### Writeup by Trent (teerix)



### Level 0

Upon logging into leviathan0 through SSH (`ssh -l leviathan0 -p 2223 leviathan.labs.overthewire.org`) and issuing `ls -al` shows a hidden `.backup` directory, containing a `bookmarks.html` file. Using `cat` on this file normally produces too much output, so I issued a grep for "leviathan".

`cat bookmarks.html | grep "leviathan"`

This returns the following:

```html
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

Level 1 Password: rioGegei8m



### Level 1

Logging into leviathan1 and listing the files in the home directory shows a binary file named `check`. Running it normally asks you to input a password, and if correct, you will receive a shell. Running an ltrace and inputting any string for the "password" prompt shows that `strcmp()` is used, with the string "sex" being compared to. After running the binary normally, using "sex" as the password, and receiving the shell, issuing `whoami` shows that you are now leviathan2. You now have access to the password at `/etc/leviathan_pass/leviathan2`


Level 2 Password: ougahZi8Ta



### Level 2

The home directory of level 2 contains a `printfile` binary, which takes a file and checks if there is read-access using `access()`, then appends the file to a string containing `/bin/cat`, then does a system call with the newly created string. Since this file is owned by leviathan3, and that `access()` and `system()` use the process' real UID, it is very useful for privesc into the leviathan3!

Firstly we need to create a file that matches our goal command we want to call to system, so we will create two files "junk" and "junk;bash". The `access()` call with look at the full filename "junk;bash" as a whole, while our system call will look like `/bin/cat junk;bash`, so only the contents in "junk" (it will be empty) will be displayed, and a shell in leviathan3's name will be spawned!

```sh
leviathan2@leviathan:/tmp/teerix$ touch junk
leviathan2@leviathan:/tmp/teerix$ touch "junk;bash"
leviathan2@leviathan:/tmp/teerix$ ~/printfile "junk;bash"
leviathan3@leviathan:/tmp/teerix$ cat /etc/leviathan_pass/leviathan3
Ahdiemoo1j
```

Level 3 Password: Ahdiemoo1j

