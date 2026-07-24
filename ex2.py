count=int(input("How many devices?"))
devices=[]
for i in range(count):
    hostname = input("Enter Hostname")
    ip= input("Enter IP :")
    devices.append((hostname,ip))
def backup(hostname,ip):
    print(f"connecting to {hostname},{ip}")
    return "success"

success=0
failed=0

for hostname,ip in devices:
    result=backup(hostname,ip)
    if result =="success":
        success+=1
    else:
        failed+=1
print("=======================Summary===========================")
print("Total Devices",len(devices))
print("Success :",success)
print("Failed :",failed)
