count=int(input("Enter the No.of devices"))
devices=[]
for i in range(count):
    hostname=input("Enter the hostname :")
    ip=input("Enter the IP Address :")
    devices.append((hostname,ip))

def dev_srch(ip):
    if ip=="10.1.1.1":
        return "Device Found"
    elif ip=="10.1.1.2": 
        return "Device Found"
    elif ip=="10.1.1.3":
        return "Device Found"
    else:
        return "Device Not Found"

success=0
failed=0

for hostname,ip in devices:
    result=dev_srch(ip)
    print(f"{hostname},({ip}):{result}")
    if result=="Device Found":
        success+=1
    else:
        failed+=1
print("===================Inventory Tool=========================")
print("="*40)
print("Total No.of devices :",len(devices))
print("Total No. of Devices Found :",success)
print("Total No. of Devices not Found :",failed)