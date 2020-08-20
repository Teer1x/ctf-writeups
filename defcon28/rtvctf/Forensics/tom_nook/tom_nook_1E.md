## Tom Nook 1E
### Writeup by Trent (teerix)

Category: Forensics

```
Are you able to crack the zip file? What's the password?
```

When examining the TCP stream of the ZIP files in Wireshark, change the "Show and save data as" section to Raw bytes, and save the stream as any name.

Now we want to extract the ZIP file from the overall stream. There are two primary methods of doing this, `dd` and `binwalk`.

Issuing `binwalk -e (file_name)` and viewing the extracted files will give you a password-protected ZIP
file. I used rockyou.txt and `fcrackzip` to find the password.

`fcrackzip -u -D -p rockyou.txt (file_name)`

The password to the file is monkey123.

Flag: monkey123