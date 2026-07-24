search_ip=input("Enter the ip address to find the details")

devices=[
    {"hostname":"R1","IP":"10.1.1.1","Location":"Chennai"},
    {"hostname":"R2","IP":"10.1.1.2","Location":"Mumbai"},
    {"hostname":"R3","IP":"10.1.1.3","Location":"Dubai"},
    {"hostname":"SW1","IP":"10.1.1.4","Location":"Sydney"}
]

found = False 

for device in devices:
    if search_ip==device["IP"]:
        found=True
        print("Device found")

        print(device["hostname"])
        print(device["IP"])
        print(device["Location"])
        break
if found==False:
     print("Device NOT Found ")
        