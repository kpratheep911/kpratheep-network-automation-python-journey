ip=input("Enter the ip address")
octets=ip.split(".")
print(octets)
private_ip=False
first_octet=int(octets[0])
second_octet=int(octets[1])
if octets[0]=="172" and 16<=second_octet <=31:
    private_ip=True
if octets[0]=="10":
    private_ip=True
if octets[0]=="192" and octets[1]=="168":
    private_ip=True
if private_ip==True:
    print("Private ip")
else:
    print("public ip")
