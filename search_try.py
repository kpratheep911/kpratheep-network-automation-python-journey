
devices=["SW1","SW2","SW3"]
search=input("Enter your device")
found=False
try:
    for device in devices:
       # print(device)
        if search.lower()==device.lower():
             #print("Device found")
             found=True
    if found==True:
          print(f"{search} device found")
    else:
          print(f"{search} not found")

except ValueError:
        print("Invalid Entry ")
finally:
        print("Devices stored in inventory")