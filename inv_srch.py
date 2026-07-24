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

print(f"Total devices loaded: {len(devices)}")

# Filter by location
search = input("\nEnter location to search: ")

print("\nResults:")
print("=" * 50)

for device in devices:
    if device["location"].lower() == search.lower():
        print(f"{device['hostname']:<14} "
              f"{device['ip']:<14} "
              f"{device['type']:<10} "
              f"{device['location']}")

print("=" * 50)