try:
    with open("newdevices.txt","r") as file:
        devices=file.read()
        print(devices)
except:
        print("Inventory file not found")
finally:
       print("Program Completed")