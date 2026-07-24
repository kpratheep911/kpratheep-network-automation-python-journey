devices = [
    {"hostname":"Router1", "ip":"192.168.10.1", "status":"UP"},
    {"hostname":"Router2", "ip":"192.168.10.2", "status":"DOWN"},
    {"hostname":"SW1",     "ip":"192.168.10.3", "status":"UP"},
    {"hostname":"SW2",     "ip":"192.168.10.4", "status":"DOWN"},
    {"hostname":"FW1",     "ip":"192.168.10.5", "status":"UP"},
]

with open("exxon_report.txt", "a") as f:
    f.write("Exxon Mobil Network Report\n")
    f.write("=" * 40 + "\n")
    
    for device in devices:
        line = f"{device['hostname']:<10} | {device['ip']:<16} | {device['status']}\n"
        f.write(line)
    
    f.write("=" * 40 + "\n")
    f.write(f"Total devices: {len(devices)}\n")

print("✅ Exxon Mobil Report saved!")