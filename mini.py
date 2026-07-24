import os
os.system("cls")

devices=[]
def add_device():
    device=input("Enter the device name :")
    devices.append(device)
    print("Device Added Successfully")
    print("Total No. of devices in the list :" ,len(devices))
def show_device():
    if not devices:
        print("No devices in the list")
        return
    print("List of devices:")
    for device in devices:
        print(device)
def search_device():
    device=input("Enter the device name to search")
    if device in devices:
        print("Device Found")
        print("Row Number of the device in the list is :",devices.index(device)+1)
    else:
        print("Device Not Found")
def remove_device():
    device=input("Enter the device name to remove")
    if device in devices:
        devices.remove(device)
        print("Device Removed Successfully")
        print("Total No. of devices in the list :" ,len(devices))
    else:
        print("Device Not Found")
def ip_check():
    ip=input("Enter the IP address to check")
    octets=ip.split(".")
    if len(octets)!=4:
        print("Invalid IP address")
        return
    for octet in octets:
        if not octet.isdigit() or int(octet)<0 or int(octet)>255:
            print("Invalid IP address")
            return
    print("Valid IP address")
    private_ip=False
    first_octet=int(octets[0])
    second_octet=int(octets[1])
    if first_octet==10:
        private_ip=True
    elif first_octet==172 and second_octet>=16 and second_octet<=31:
        private_ip=True
    elif first_octet==192 and second_octet==168:
        private_ip=True
    if private_ip:
        print("But it is a Private IP address")
    else:
        print("But it is a Public IP address")
def device_count():
    print("Total No.of devices in the list :",len(devices))
def ping_check():
    ip=input("Enter the IP address to ping :")
    response=os.system("ping -n 2 "+ip)
    if response==0:
        print(ip,"is reachable") 
    else:
        print(ip,"is not reachable")
def exit_program():
    print("Exiting the program")
    

print("\t\tWelcome to the Mini Network Automation tool")
print("\t\t=========================================")
while True:
    print("1. Add Device")
    print("2. Show Devices")
    print("3. Search Device")
    print("4. Remove Device")
    print("5. Device Count")
    print("6. Check IP Address")
    print("7. ping Check")
    print("8. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_device()
    elif choice=="2":
        show_device()
    elif choice=="3":
        search_device()
    elif choice=="4":
        remove_device()
    elif choice=="5":
        device_count()
    elif choice=="6":
        ip_check()
    elif choice=="7":
        ping_check()
    elif choice=="8":
        exit_program()
        break    
    else:
        print("Invalid Choice")