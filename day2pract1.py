devices = [

	{"hostname":"R1","Vendor":"cisco","loc":"chennai","type":"ios"},
	{"hostname":"R2","Vendor":"cisco","loc":"chennai","type":"ios"},
	{"hostname":"R3","Vendor":"cisco","loc":"chennai","type":"ios"},
	{"hostname":"R4","Vendor":"cisco","loc":"chennai","type":"ios"},
	{"hostname":"R5","Vendor":"cisco","loc":"chennai","type":"ios"},
	{"hostname":"SW1","Vendor":"cisco","loc":"chennai","type":"nxos"},
	{"hostname":"SW2","Vendor":"cisco","loc":"chennai","type":"nxos"},
	{"hostname":"SW3","Vendor":"cisco","loc":"chennai","type":"nxos"}
]

print("\n My Chennai Inventory...\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

for device in devices:
	if device["loc"]=="chennai":
	    print("Connecting to Chennai devices...",device["hostname"], " | Vendor", device["Vendor"] , " | Loc", device["loc"], " | OS-Type", device["type"])
print("Total devices :",len(devices))
