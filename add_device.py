import os
os.system("cls")
#Print title of the program
print("Adding devices in the list && Displaying all devices in the list")
devices=[]
#get input from user

while True:
    device=input("Enter the device name")
    devices.append(device)
    print("Do you want to add another device in the list?(Yes/No)")
    choice=input("\nChoose your option :[yes/no]")
    if choice=="no":
        break
    if choice=="yes":
        continue
print(" Device List below")
print("="*20)
for device in devices:        
    print(device)
print("\n")
print("Total No. of devices in the list :" ,len(devices))


while True:
    choice=input(" Do you want to search your device : [yes/no]")
    found=False
    if choice=="yes":        
        search=input("Enter the hostname to search")
        for device in devices:
            if device.lower()==search.lower():
                print("Device is found")
                found=True

        if found==False:
            print("Device not found")
            

    elif choice=="no":
        print("Thank you")
        break 
    else:
        print("Invalid Choice")

 

