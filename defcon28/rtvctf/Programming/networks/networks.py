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
