import openpyxl

wb = openpyxl.load_workbook("network_inventory.xlsx")
ws = wb.active

# Load all devices
devices = []
for row in ws.iter_rows(min_row=2, values_only=True):
    device = {
        "hostname" : row[0],
        "ip"       : row[1],
        "type"     : row[2],
        "vendor"   : row[3],
        "model"    : row[4],
        "location" : row[5],
    }
    devices.append(device)

print(f"\nTotal devices loaded: {len(devices)}")

# Menu
print("\nFilter by:")
print("1. Hostname")
print("2. IP Address")
print("3. Device Type")
print("4. Location")

choice = input("\nEnter choice (1-4): ")

if choice == "1":
    search = input("Enter hostname: ")
    field  = "hostname"
elif choice == "2":
    search = input("Enter IP address: ")
    field  = "ip"
elif choice == "3":
    search = input("Enter device type (Router/Switch/Firewall): ")
    field  = "type"
elif choice == "4":
    search = input("Enter location: ")
    field  = "location"
else:
    print("Invalid choice!")
    field  = None
    search = None

# Filter and show results
if field and search:
    results = []
    for device in devices:
        if str(device[field]).lower() == search.lower():
            results.append(device)

    if results:
        print(f"\nFound {len(results)} devices:")
        print("=" * 55)
        print(f"{'Hostname':<14} {'IP':<14} {'Type':<10} {'Location'}")
        print("-" * 55)
        for device in results:
            print(f"{str(device['hostname']):<14} "
                  f"{str(device['ip']):<14} "
                  f"{str(device['type']):<10} "
                  f"{str(device['location'])}")
        print("=" * 55)
    else:
        print(f"\nNo devices found!")