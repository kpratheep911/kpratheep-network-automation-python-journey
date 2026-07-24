devices=[
    {"hostname":"R1","IP":"10.1.1.1","dev_type":"Cisco","Location":"Chennai"},
    {"hostname":"R2","IP":"10.1.1.2","dev_type":"Cisco","Location":"Chennai"},
    {"hostname":"SW1","IP":"10.1.1.3","dev_type":"Cisco","Location":"Berlin"},
    {"hostname":"SW2","IP":"10.1.1.4","dev_type":"PaloAlto","Location":"Sydney"}
    ]
print("\n Search by :")
print("1. Hostname")
print("2. IP Address")
print("3. Device Type")
print("4. Location")

choice=input("Enter choice(1-4):")

if choice=="1":
    search=input("Enter hostname    :")
    field="hostname"
elif choice=="2":
    search=input("Enter IP          :")
    field="IP"
elif choice=="3":
    search=input("Enter Dev_Type    :")
    field="dev_type"
elif choice=="4":
    search=input("Enter Location    :")
    field="Location"
found = False
for device in devices:
    if device[field].lower()==search.lower():
        print("="*50)
        print(f"\t   {device[field]} is found")
        print("-"*50)
        print(f"Host name     : {device['hostname']}")
        print(f"IP Address    : {device['IP']}")
        print(f"Device Type   : {device['dev_type']}")
        print(f"Location      : {device['Location']}")
        print("="*50)  
        found=True
if found==False:
    print("device not found")