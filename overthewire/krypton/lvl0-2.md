## OverTheWire Krypton

### Writeup by Trent (teerix)



### Level 0

The base64 string "S1JZUFRPTklTR1JFQVQ=" is given to you, and you simply have to decode it to obtain the level 1 password.

`echo "S1JZUFRPTklTR1JFQVQ=" | base64 -d`

Level 1 Password: KRYPTONISGREAT



### Level 1

```
The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!
```

The "krypton2" file being references has the ciphertext `YRIRY GJB CNFFJBEQ EBGGRA` within it. The simple rotation used it ROT-13, where each letter is substituted with the letter 13 characters down from its position. This decodes into `LEVEL TWO PASSWORD ROTTEN`.

Level 2 Password: ROTTEN



### Level 2

```
The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.

One shot can solve it!

Have fun.
```

The ciphertext in "krypton3" is `OMQEMDUEQMEK`.

When using a non-brute-force method to solve this, the best way to go about is by using an A-Z padding and giving it to the encryption program given to determine the offsets.

```sh
krypton2@krypton:/tmp/tmp.fZgVgb7mqo$ echo "ABCDEFGHIJKLMNOPQRSTUVWXYZ" > pad
krypton2@krypton:/tmp/tmp.fZgVgb7mqo$ /krypton/krypton2/encrypt pad 
krypton2@krypton:/tmp/tmp.fZgVgb7mqo$ ls
ciphertext  keyfile.dat  pad
krypton2@krypton:/tmp/tmp.fZgVgb7mqo$ cat ciphertext
MNOPQRSTUVWXYZABCDEFGHIJKL
```

As you can see ABC...XYZ turned into MNO...JKL, which indicates a rotation of 12. Using this, the ciphertext decodes to `CAESARISEASY`.

Level 3 Password: CAESARISEASY



### Level 3

```
Well done. You’ve moved past an easy substitution cipher.

The main weakness of a simple substitution cipher is repeated use of a simple key. In the previous exercise you were able to introduce arbitrary plaintext to expose the key. In this example, the cipher mechanism is not available to you, the attacker.

However, you have been lucky. You have intercepted more than one message. The password to the next level is found in the file ‘krypton4’. You have also found 3 other files. (found1, found2, found3)

You know the following important details:

    The message plaintexts are in English (*** very important) - They were produced from the same key (*** even better!)

Enjoy.
```

Essentially we are using frequency analysis to figure out what each ciphertext letter corresponds to which plaintext letter based on how often it occurs.

Using the few large ciphertexts included, I eventually deduced that the decrypt alphabet is `QAZWSXEDCRFVTGBYHNUJMIKOLP`.

```sh
krypton3@krypton:/krypton/krypton3$ cat krypton4 | tr QAZWSXEDCRFVTGBYHNUJMIKOLP ABCDEFGHIJKLMNOPQRSTUVWXYZ
WELLD ONETH ELEVE LFOUR PASSW ORDIS BRUTE 
```

Level 4 Password: BRUTE