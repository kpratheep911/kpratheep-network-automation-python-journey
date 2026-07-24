import openpyxl

wb = openpyxl.load_workbook("network_inventory.xlsx")
ws = wb.active

print("\nNetwork Inventory")
print("=" * 55)
print(f"{'Hostname':<10} {'IP':<14} {'Type':<10} {'Location'}")
print("-" * 55)

for row in ws.iter_rows(min_row=2, values_only=True):
    hostname = row[0]
    ip       = row[1]
    dev_type = row[2]
    location = row[5]
    
    print(f"{hostname:<10} {ip:<14} {dev_type:<10} {location}")

print("=" * 55)