# ═══════════════════════════════════════
# Network Inventory - Smart Edition
# Combines: Lists, Loops, Dictionaries,
#           Functions, if/elif/else
# ═══════════════════════════════════════

devices = [
    {"hostname":"R1",  "ip":"192.168.10.1", "os":"ios",  "vendor":"cisco"},
    {"hostname":"R2",  "ip":"192.168.10.2", "os":"ios",  "vendor":"cisco"},
    {"hostname":"SW1", "ip":"192.168.10.3", "os":"nxos", "vendor":"cisco"},
    {"hostname":"SW2", "ip":"192.168.10.4", "os":"nxos", "vendor":"cisco"},
    {"hostname":"FW1", "ip":"192.168.10.5", "os":"asa",  "vendor":"cisco"},
    {"hostname":"EX1", "ip":"192.168.10.6", "os":"junos","vendor":"juniper"},
]

def identify_device(hostname, ip, os):
    if os == "ios":
        device_type = "Cisco Catalyst Router"
    elif os == "nxos":
        device_type = "Cisco Nexus Switch"
    elif os == "asa":
        device_type = "Cisco Firewall"
    else:
        device_type = "Unknown Device"

    print(f"\n  Hostname : {hostname}")
    print(f"  IP       : {ip}")
    print(f"  Type     : {device_type}")
    print("  " + "-" * 33)

# ═══════════════════════════════════════
print("\n" + "═" * 37)
print("   SMART NETWORK INVENTORY REPORT")
print("═" * 37)

for device in devices:
    identify_device(device["hostname"],
                    device["ip"],
                    device["os"])

print(f"\n  Total devices: {len(devices)}")
print("═" * 37)