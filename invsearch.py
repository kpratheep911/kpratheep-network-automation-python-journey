# ================================================
# Network Device Lookup Tool
# Exxon Mobil
# ================================================

import openpyxl

# ================================================
# CONFIGURATION
# ================================================
INVENTORY_FILE = "network_inventory.xlsx"

# ================================================
# FUNCTION 1 - Read inventory from Excel
# ================================================
def load_inventory(filename):
    devices = []
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    
    for row in ws.iter_rows(min_row=2, values_only=True):
        device = {
            "hostname"    : row[0],
            "ip"          : row[1],
            "device_type" : row[2],
            "vendor"      : row[3],
            "location"    : row[4],
            "serial"      : row[5]
        }
        devices.append(device)
    
    return devices

# ================================================
# FUNCTION 2 - Search device by IP
# ================================================
def search_by_ip(devices, search_ip):
    for device in devices:
        if str(device["ip"]) == search_ip:
            return device
    return None

# ================================================
# FUNCTION 3 - Display device details
# ================================================
def show_device(device):
    print("\n" + "=" * 45)
    print("         DEVICE DETAILS")
    print("=" * 45)
    print(f"Hostname    : {device['hostname']}")
    print(f"IP Address  : {device['ip']}")
    print(f"Device Type : {device['device_type']}")
    print(f"Vendor      : {device['vendor']}")
    print(f"Location    : {device['location']}")
    print(f"Serial No   : {device['serial']}")
    print("=" * 45)

# ================================================
# MAIN PROGRAM
# ================================================
print("\n" + "=" * 45)
print("   NETWORK DEVICE LOOKUP TOOL")
print("   Exxon Mobil")
print("=" * 45)

# Load inventory
devices = load_inventory(INVENTORY_FILE)
print(f"\nInventory loaded: {len(devices)} devices")

# Ask user for IP
ip = input("\nEnter IP address to search: ")

# Search for device
device = search_by_ip(devices, ip)

# Show result
if device:
    show_device(device)
else:
    print(f"\nDevice {ip} not found in inventory!")