print(" Network Inventory tool")
print("="*20)

def check_device(hostname,ip):
	print("The hostname is :",hostname)
	print("The ip address is :",ip)

check_device("SW1","10.1.1.1")
check_device("R1","10.1.1.1")
check_device("R2","10.1.1.2")