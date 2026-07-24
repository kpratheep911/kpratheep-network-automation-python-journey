count=int(input("Enter the no. of devices"))
devices=[]
for i in range(count):
    hostname=input("Enter the Hostname :")
    ip=input("Enter the ip address :")
    devices.append((hostname,ip))

def ping_check(ip):
    if ip=="10.1.1.1":
        return "failed" 
    else:
        return "Success"
    
success=0
failed=0

for hostname,ip in devices:
    result=ping_check(ip)
    print(f"{hostname} ({ip}) : {result}")
    if result == "Success":
        success+=1
    else:
        failed+=1
print("=============Summaey================")
print("Total No.of devices",len(devices))
print("Total No. of ping Success :",success)
print("Total No.of ping failed :",failed)