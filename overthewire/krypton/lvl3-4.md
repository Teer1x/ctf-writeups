## OverTheWire Krypton

### Writeup by Trent (teerix)




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



### Level 4

```
This level is a Vigenère Cipher. You have intercepted two longer, english language messages. You also have a key piece of information. You know the key length!

For this exercise, the key length is 6. The password to level five is in the usual place, encrypted with the 6 letter key.
```

This is very simple to brute force using any online tool, but it was a bit more fun using frequency analysis and our own script on the given `found1` and `found2` files that are included with this challenge.

Since the key length of the Vigenere cipher is 6, it means that every sixth letter is encoded using the same letter, meaning we can do frequency analysis on every sixth letter for each place value of the key, and determine offsets looking at several of the most commonly used letters. The script below I created, piped into the `more` command is very useful for this.

```py
import collections
import itertools

key_length = 6
common_letters = ['E','T','A', 'I']
ciphertext = ''
combos = {}
with open("found1", "r") as f:
    ciphertext = f.read().strip().replace(' ', '').upper()


for offset in range(key_length):
    key = ciphertext[offset::key_length]
    common_letter = collections.Counter(key).most_common(1)[0][0]
    combos[offset] = [chr((((ord(common_letter) - 65) - (ord(x) - 65)) % 26) + 65) for x in common_letters]

possible_keys = list(itertools.product(*list(combos.values())))

keys_padded = []
for k in possible_keys:
    keys_padded.append((k * (len(ciphertext) // len(k) + 1))[:len(ciphertext)])


plaintexts = []
for k in keys_padded:
    plaintext = ''
    for cipher, kval in zip(ciphertext, k):
        plaintext += chr((((ord(cipher) - 65) - (ord(kval) - 65)) % 26) + 65)

    if plaintext not in plaintexts:
        plaintexts.append(plaintext)

print("Possible Plaintexts:")
for i in range(len(possible_keys)):
    print(f"Using key: {''.join(possible_keys[i])}")
    print(plaintexts[i], end="\n\n")

print(plaintext)
```

The first result uses the key `FREKEY` and it completely decodes the message. When used on the ciphertext for the next level's password, we receive the plaintext `CLEAR TEXT`

Level 5 Password: CLEARTEXT