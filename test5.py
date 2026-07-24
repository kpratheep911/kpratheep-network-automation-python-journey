devices=["R1","R2","R3","R4","R5"]

with open("devices1.txt","w")as f:
	for device in devices:
		f.write(device +"\n")
print("File Saved")
