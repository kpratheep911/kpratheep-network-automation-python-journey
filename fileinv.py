devices = [
    {"hostname":"R1",  "ip":"10.1.1.1", "status":"UP"},
    {"hostname":"R2",  "ip":"10.1.1.2", "status":"DOWN"},
    {"hostname":"SW1", "ip":"10.1.1.3", "status":"UP"},
    {"hostname":"SW2", "ip":"10.1.1.4", "status":"DOWN"},
    {"hostname":"FW1", "ip":"10.1.1.5", "status":"UP"},
]

def save_report(devices, filename):
    with open(filename, "w") as f:
        f.write("My Network Inventory\n")
        f.write("=" * 30 + "\n")
        for device in devices:
            f.write(f"{device['hostname']} - {device['ip']}\n")
        f.write(f"Total devices: {len(devices)}\n")
    print(f"File saved to {filename}")

def read_report(filename):
    with open(filename, "r") as f:
        content = f.read()
    print(content)

save_report(devices, "final_report.txt")
read_report("final_report.txt")