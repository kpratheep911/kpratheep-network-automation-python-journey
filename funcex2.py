def show_devices(device_type, devices):
    print("\n---", device_type, "---")
    for device in devices:
        print(device)

routers  = ["cisco", "juniper", "Aruba"]
switches = ["catalyst", "nexus", "leaf"]
firewalls = ["ASA", "Firepower", "Palo Alto"]

show_devices("ROUTERS",   routers)
show_devices("SWITCHES",  switches)
show_devices("FIREWALLS", firewalls)