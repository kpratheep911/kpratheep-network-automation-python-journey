devices = [
    {"hostname":"R1", "ip":"10.0.0.1"},
    {"hostname":"R2", "ip":"10.0.0.2"},
    {"hostname":"R3", "ip":"10.0.0.3"},
]

success = []
failed  = []

for device in devices:
    try:
        print(f"Connecting to {device['hostname']}...")
        
        if device["hostname"] == "R2":
            raise Exception("Connection timed out!")
        
        print(f"✅ {device['hostname']} - Success!")
        success.append(device["hostname"])
        
    except Exception as e:
        print(f"❌ {device['hostname']} - Failed: {e}")
        failed.append(device["hostname"])

# Save report
with open("change_report.txt", "w", encoding="utf-8") as f:
    f.write("CHANGE REPORT\n")
    f.write("=" * 40 + "\n\n")
    
    f.write("✅ SUCCESSFUL DEVICES:\n")
    for device in success:
        f.write(f"  {device}\n")
    
    f.write(f"\nTotal Success: {len(success)}\n")
    
    f.write("\n❌ FAILED DEVICES:\n")
    for device in failed:
        f.write(f"  {device}\n")
    
    f.write(f"\nTotal Failed: {len(failed)}\n")

print("\n" + "=" * 40)
print(f"✅ Success : {len(success)}")
print(f"❌ Failed  : {len(failed)}")
print("📄 Report saved to change_report.txt") 