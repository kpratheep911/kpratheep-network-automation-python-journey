import openpyxl

def load_inventory(filename):
    devices = []
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    for row in ws.iter_rows(min_row=2, values_only=True):
        device = {
            "hostname" : row[0],
            "ip"       : row[1],
            "dev_type" : row[2],
            "vendor"   : row[3],
            "model"    : row[4],
            "location" : row[5],
            "country"  : row[6],
            "sitecode" : row[7],
            "serial"   : row[8],
        }
        devices.append(device)
    return devices

def show_all(devices):
    print("\n" + "=" * 60)
    print(f"{'Hostname':<14} {'IP':<14} {'Type':<12} {'Location'}")
    print("-" * 60)
    for device in devices:
        print(f"{str(device['hostname']):<14}"
              f"{str(device['ip']):<14}"
              f"{str(device['dev_type']):<12}"
              f"{str(device['location'])}")
    print("=" * 60)
    print(f"Total: {len(devices)} devices")

# Load inventory
devices = load_inventory("network_inventory.xlsx")
print(f"Inventory loaded: {len(devices)} devices")

# Menu
print("\nSearch by:")
print("1. Hostname")
print("2. IP Address")
print("3. Device Type")
print("4. Location")
print("5. Show ALL devices")

choice = input("\nEnter choice (1-5): ")

if choice == "1":
    search = input("Enter hostname    : ")
    field  = "hostname"
elif choice == "2":
    search = input("Enter IP          : ")
    field  = "ip"
elif choice == "3":
    search = input("Enter Device Type : ")
    field  = "dev_type"
elif choice == "4":
    search = input("Enter Location    : ")
    field  = "location"
elif choice == "5":
    show_all(devices)

if choice != "5":
    found = False
    for device in devices:
        if str(device[field]).lower() == search.lower():
            print("=" * 50)
            print(f"  {search} is found!")
            print("-" * 50)
            print(f"Hostname  : {device['hostname']}")
            print(f"IP        : {device['ip']}")
            print(f"Type      : {device['dev_type']}")
            print(f"Model     : {device['model']}")
            print(f"Location  : {device['location']}")
            print(f"Country   : {device['country']}")
            print(f"Serial    : {device['serial']}")
            print("=" * 50)
            found = True

    if not found:
        print(f"\nSorry! {search} not found!")