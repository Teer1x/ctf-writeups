## Strings

### Writeup by Trent (teerix)

Category: Pwn

```
strings the attached file or maybe you can't, I don't know what I'm doing.

File Included: strings.s
```

You are given an assembly file "strings.s" (included with the writeup). Performing the "strings" command on this file itself
results in the same output as if "cat" was used instead.

However, if you compile it into an executable with `gcc strings.s -o stringfile` then do `strings stringfile`, you can see a majority of the flag from this, with a few characters missing.

Using `hexdump -C stringfile` gave me the remaining few characters of the flag.


Flag: ts{DidYouUseStringsorMaths}

