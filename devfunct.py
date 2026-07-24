print("Network Inventory Tool")

def menu():
	print("1. Add Devices")
	print("2. Show Devices")
	print("3. Exit")
	

devices=[]
choice = int(input(" Choose options from the menu [1-3]"))

while True:
    if choice == 1:
        add_device()

    elif choice==2:
        print(devices)

    elif choice==3:
        print("Thank you")
        break

    else:
	    print("Invalid option")


def add_device():
	dev=input(" Enter the device name")
	devices.append(dev)
	print("device added")
	choice1 = input("Do you want to add another device (yes/no)")
 if choice1=="yes":
	dev=input(" Enter the device name")
devices.append(dev)
    elif choice1=="no":
	    print("return to menu")
    
menu()