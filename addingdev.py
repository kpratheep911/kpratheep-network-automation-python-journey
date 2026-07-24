print("="*145)
print("\t\t\t\t\t                    Network Inventory Tool")
print("="*145)
devices=[]

def menu():
    print(" Choose option from the menu")
    print(" 1. Add Devices")
    print(" 2. Show Devices")
    print(" 3. Exit")

while True:    
    menu()
    print("-"*60)
    option_menu=int(input("Choose option from the menu [1-3]: "))    
    print("-"*60) 
    count=0                  
    if option_menu==1:
          
          while True:
            
            device=input("Enter the device name")
            devices.append(device)
            print(f"{'device'} is added ")
            count+=1
            print("Total No.of devices in the list",count)
            choice = input("Do you want to add another device Yes/No :")       
            if choice.lower()=="no":
                 break
            elif choice.lower()=="yes":
                 continue
            else:
                 print("The choice is invalid.Enter yes/no")
    
    elif option_menu==2:
        print(" Total No.of devices in the list : ",count)
        for device in devices:      
            print(device)
   
    elif option_menu==3:
        print(" Thank you")
        break
     
    else:
        print("Invalid Option")
 