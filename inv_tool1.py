print("             Network Inventory Tool")
print("="*50)
devices=[]
while True:
    print("Menu")
    print("-"*7)
    print("1.Add Device")
    print("2.Show the devices")
    print("3.Exit")
    choice=int(input("Enter your choice[1-3]"))
    if choice==1:        
        device=input("Enter the device")
        devices.append(device)
        print("Device Added")
        choice1=input(" Do you want add another device yes or no :")
        if choice1=="yes":
            
    elif choice==2:
        for device in devices:
            print(device)
    elif choice==3:
        print("Thank You")
        break
    else :
        print("Invalid Input. Please Try Again ")
       

