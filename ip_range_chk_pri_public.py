ip=input("Enter the ip address")
octets=ip.split(".")
print(octets)
private_ip=False
first_octet=int(octets[0])
second_octet=int(octets[1])
if first_octet==172 and 16<=second_octet <=31:
    private_ip=True
elif first_octet==10:
    private_ip=True
elif first_octet==192 and second_octet==168:
    private_ip=True
if private_ip==True:
    print("Private ip")
else:
    print("public ip")
