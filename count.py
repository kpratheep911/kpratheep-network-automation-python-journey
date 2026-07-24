with open("inventory.txt","r") as f:
 
    count=0-2
    for line in f: 
            count+=1
print("Total No. Of Devices :",count)

with open("inventory.txt","r") as f:
       content=f.read()
print(content)