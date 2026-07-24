import openpyxl

wb = openpyxl.load_workbook("network_inventory.xlsx")
ws = wb.active

print("Network Inventory")
print("=" * 50)
print(f"{'Hostname':<14} {'IP':<14} {'Type':<10} {'Location'}")
print("-" * 50)

for row in ws.iter_rows(min_row=2, values_only=True):
    hostname = row[0]
    ip       = row[1]
    dev_type = row[2]
    location = row[5]
    print(f"{hostname:<14} {ip:<14} {dev_type:<10} {location}")

print("=" * 50)