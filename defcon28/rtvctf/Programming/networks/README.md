## Networks

### Writeup by Trent (teerix)

Category: Programming

```
We have a new intern that proposed some ip addresses to deploy in our network. 
We think the intern was off by a few bits when generating the addresses.

For each pair of IP address and its paired subnet determine if the IP address is a valid address in the subnet.

Provide the total count of valid IP addresses in subnet.

Warning: Max submissions is 10

File Included: ipaddress.txt
```

Solution:

The challenge gives us a txt file of many lines (file included with this writeup), with each line in the form [ip_addr],[network]/[CIDR mask]. The
goal is to figure out how many lines have proper IP addresses associated with the given network address and subnet.

This challenge is very easy when using Python and the ipaddress library; no need to split ip address and do bitwise operations.

Here is my script below to count the number of proper IP address for each subnet.

```py
from ipaddress import ip_network, ip_address


ip_count = 0

with open('ipaddress.txt', 'r') as f:
	lines = f.readlines()

	for line in lines:
		ip, netsub = line.split(',')
		net = ip_network(netsub.strip())
		if ip_address(ip.strip()) in net:
			ip_count += 1

print(ip_count)
```

Flag: 48
