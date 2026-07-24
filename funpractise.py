print("\t\t                  Network Inventory Tool")
print("="*100)
devices=[]
def add_device():
   device=input("Enter your device name to add in the list :")
   devices.append(device)
   return device

add_device()
add_device()
add_device()
for device in devices:
    print(device)
print("-"*40)
print("Devices added in the list")
print("-"*40)