## Tom Nook 1A
### Writeup by Trent (teerix)

Category: Forensics

```
There's been suspicion that Tom Nook has been exfiltrating data out of the network. Could you help me find out what he's doing? Attached is a PCAP.
```

This is one of the more vague challenges of the bunch. When viewing the PCAP in Wireshark, there are two HTTP data streams that show data exfiltration occurring.

When examining the TCP or HTTP stream of the first stream (Packets 1-15, right-click any packet, hover over "Follow", click "Follow TCP Stream"), you can see that one of the files exfiltrated is `flag.txt` with a flag as the contents, which is the flag for this challenge.

Flag: TS{TomNookUsesTheInternet}
