location=input("Enter the location to find all the devices  : ")
devices=[
    {"hostname":"R1","IP":"10.1.1.1","Location":"Chennai"},
    {"hostname":"R5","IP":"10.1.1.10","Location":"Chennai"},
    {"hostname":"R2","IP":"10.1.1.2","Location":"Mumbai"},
    {"hostname":"R3","IP":"10.1.1.3","Location":"Dubai"},
    {"hostname":"SW1","IP":"10.1.1.4","Location":"Sydney"}
]

found = False
print("="*40)
print(" Location Based Inventory")
print("="*40)
for device in devices:
 
    if location==device["Location"]:
       found =True
       print(f"Location :",device["Location"])
       print("Hostname :",device["hostname"])
       print("IP :",device["IP"])
       print("-"*40)
       
print("="*40)
if found ==False :
    print("unknown Location")