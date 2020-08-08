## 1 - Pop a shell on that

### Writeup by Trent (teerix)

Category: Workout at Home Gym

```
http://164.90.147.56:8081/

I bet you can pop a shell, pretty easily on this site. I left something for you in the root of the filesystem.
research will get you farther than Burp
PLEASE DO NOT NMAP, SQLMAP, WPSCAN, etc the site. You only need a web browser to gather the information you need to exploit. 
```

Upon coming to the given website I noticed that in the copyright, it showed the software used as
"Gym Management System 1.0". Researching this lead me to this page, https://www.exploit-db.com/exploits/48506, which discusses
an unauthenticated RCE vulnerability in this software. I used the script given there (included with this writeup), with a few tweaks.

Running the script gave me a shell, and doing `ls /` showed that there was a "flag.txt" file there.

Doing `cat /flag.txt` gave me the flag!

Flag: ts{ThatWasAnEasyShelltoPop}

