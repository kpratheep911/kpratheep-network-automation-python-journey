import openpyxl

# Load from Excel instead of hardcoded list
def load_inventory(filename):
    devices = []
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        device = {
            "hostname" : row[0],
            "IP"       : row[1],
            "dev_type" : row[2],
            "vendor"   : row[3],
            "model"    : row[4],
            "Location" : row[5],
            "country"  : row[6],
            "sitecode" : row[7],
            "serial"   : row[8],
        }
        devices.append(device)
    return devices

# Load inventory
devices = load_inventory("network_inventory.xlsx")
print(f"Inventory loaded: {len(devices)} devices")

# YOUR EXISTING MENU CODE BELOW
print("\n Search by :")
print("1. Hostname")
print("2. IP Address")
print("3. Device Type")
print("4. Location")

choice = input("\nEnter choice(1-4): ")

if choice == "1":
    search = input("Enter hostname    : ")
    field  = "hostname"
elif choice == "2":
    search = input("Enter IP          : ")
    field  = "IP"
elif choice == "3":
    search = input("Enter Device Type : ")
    field  = "dev_type"
elif choice == "4":
    search = input("Enter Location    : ")
    field  = "Location"

found = False
for device in devices:
    if str(device[field]).lower() == search.lower():
        print("=" * 50)
        print(f"  {search} is found")
        print("-" * 50)
        print(f"Hostname  : {device['hostname']}")
        print(f"IP        : {device['IP']}")
        print(f"Type      : {device['dev_type']}")
        print(f"Model     : {device['model']}")
        print(f"Location  : {device['Location']}")
        print(f"Country   : {device['country']}")
        print(f"Serial    : {device['serial']}")
        print("=" * 50)
        found = True

if found == False:
    print(f"\nSorry! {search} not found!")