
def add_device():
	device=input("Enter the device name to add")
	devices.append(device)
print("Device Added")
choice=input("Do you want to continue yes or no")
if choice=="yes":
    add_device()
    print("Added")
    
elif choice=="no":
    print("Thank you")
    break


def show_device():
      for device in devices:
            print(device)
devices=[]

print("Network Inventory Tool")
print("Menu")
print("="*7)
print("1.Add Device")
print("2.Show the devices")
print("3.Exit")
	
choice=input("Enter your choice")


while True:
    if choice =="1":
         add_device()
         continue			
    elif choice=="2":
	    show_device()
        
	

	