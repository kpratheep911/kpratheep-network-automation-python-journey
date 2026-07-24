with open("inventory.txt","a") as f:
    f.write("FW1 - 10.1.1.4\n")
    f.write("FW2 - 10.1.1.5\n")
print("Devices Added")

with open("inventory.txt","r") as f:
    content=f.read()
print(content)