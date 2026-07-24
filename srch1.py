devices=["Router1","Router2","Switch1","Switch2","Firewall1","Firewall2"]
search=input("Enter the hostname to search")
for device in devices:
    if device.lower()==search.lower():
        print(f"Hurray {device} Found")