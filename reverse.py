def mask_octet(ip_address):
    octet_list=ip_address.split('.')	
    octet_list[-1]='xxx'
    return '.'.join(octet_list)
	
	
ip="10.130.217.11"
masked_ip=mask_octet(ip)
print(masked_ip)