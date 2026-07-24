with open("newdevices.txt","w") as file:
    file.write("sw1\n")
with open("newdevices.txt","a") as file:
    file.write("SW2\n")
with open("newdevices.txt","r") as file:
    device=file.read()
    print(device)