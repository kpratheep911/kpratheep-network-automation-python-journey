devices=[
    {"hostname":"R1","IP":"10.1.1.1","dev_type":"Cisco","Location":"Chennai"},
    {"hostname":"R2","IP":"10.1.1.2","dev_type":"Cisco","Location":"Chennai"},
    {"hostname":"SW1","IP":"10.1.1.3","dev_type":"Cisco","Location":"Berlin"},
    {"hostname":"SW2","IP":"10.1.1.4","dev_type":"PaloAlto","Location":"Sydney"}
    ]
search=input("Enter the hostname to search  : ")
found=False
for device in devices:
    if device["hostname"].lower()==search.lower():
        print("="*60)
        print(f"\t\t\t\u2705 {search} is found ")
        print("-"*60)
        print(f"Hostname :{device['hostname']:<14}")
        print(f"IP:{device['IP']:<12}")
        print(f"Type:{device['dev_type']:<10}")
        print(f"Location:{device['Location']}")
        print("-"*60)
        found=True
if found==False:
    print(f"\u274c {search} not found")
