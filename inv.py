devices = [
	{"hostname":"R1","IP":"10.1.1.1"},
	{"hostname":"R2","IP":"10.1.1.2"},
	{"hostname":"R3","IP":"10.1.1.3"}
      ]

with open("inventory.txt","w") as f:
	f.write("Network Inventory\n")
	f.write("="*30 + "\n")
	for device in devices:
		f.write(f"{device['hostname']} - {device['IP']}\n")
		
with open("inventory.txt","r") as f:
    content=f.read()
    print(content)
print("File Saved!")