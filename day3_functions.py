# Day 3 - Function with full inventory

devices = [
    {"hostname":"R1",  "vendor":"cisco","loc":"chennai","type":"ios"},
    {"hostname":"R2",  "vendor":"cisco","loc":"chennai","type":"ios"},
    {"hostname":"SW1", "vendor":"cisco","loc":"dubai",  "type":"nxos"},
    {"hostname":"SW2", "vendor":"cisco","loc":"dubai",  "type":"nxos"},
    {"hostname":"R3",  "vendor":"cisco","loc":"london", "type":"ios"},
    {"hostname":"SW3", "vendor":"cisco","loc":"london", "type":"nxos"},
]

def show_site_inventory(devices, location):
    print("\n--- ", location.upper(), "Inventory ---")
    print("~" * 35)
    count = 0
    for device in devices:
        if device["loc"] == location:
            print("Host:", device["hostname"],
                  "| OS:", device["type"],
                  "| Vendor:", device["vendor"])
            count = count + 1
    print("Total devices in", location, ":", count)

# Now call it for every site - ONE LINE each
show_site_inventory(devices, "chennai")
show_site_inventory(devices, "dubai")
show_site_inventory(devices, "london")