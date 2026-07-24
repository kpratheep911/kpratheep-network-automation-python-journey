devices=["Router1","Router2","SW1","SW2","AP1","AP2","FW1","FW2"]
search=input("Enter the hostname to search : ")
found=False

for device in devices:
    if device.lower()==search.lower():
        print(f"Hurray we found the device :{device}")
        found=True
if found==False:
    print(f"Sorry We cant find the device {search}") 