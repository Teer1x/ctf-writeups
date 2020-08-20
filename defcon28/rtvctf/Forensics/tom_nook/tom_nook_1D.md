## Tom Nook 1D
### Writeup by Trent (teerix)

Category: Forensics

```
You found files in the PCAP! Noice! What is the full filename?
```

This challenge is looking for the filename of the second data stream (Packets 16-86). Following this TCP stream and viewing the header area of the data shows a ZIP file named `SecretACBankStatement.zip`

Flag: SecretACBankStatement.zip