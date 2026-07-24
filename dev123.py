print("Network Inventory Tool")
def menu():
	print("1. Add Devices")
	print("2. Show Devices")
	print("3. Exit")

devices=[]
while True:
        menu()
        choice = int(input(" Choose options from the menu [1-3]"))

        
        if choice == 1:
                while True:
    
                        device=input("Enter the device name")
                        devices.append(device)
                        print(f"{device} added successfully")
                        choice1=input("Do you want to add another")      
                        if choice1.lower()=="no":
                                break
                        elif choice1.lower()=="yes":
                                continue
                        else:
                                print("The choice is invalid,Please enter yes/no")
                        
                         
        elif choice==2:
                for device in devices:
                        print(device)

        elif choice==3:
                print("Thank you")
                break
        else:
	        print("Invalid option")