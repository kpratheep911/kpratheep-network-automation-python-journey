print("="*40)
print("        Inventory Tool ")
print("="*40)

with open("inventory.txt","w") as f:
	f.write("Network Inventory \n")
	f.write("="*40 +"\n")

while True:
	
	hostname=input("Enter Hostname :")
	ip =input("Enter IP Address")
	
	with open("inventory.txt","a") as f:
		f.write(f"{hostname}-{ip}\n")
	
	print("\u2705 Device Saved")

	choice =input(" Do you want to add another device? (yes/no :").lower()

	if choice=="yes":
		continue
	elif choice =="no":
		break
	else:
		print("Invalid choice.Exiting....")
		break

print("="*40)
print("Inventory Contents")
print("="*40)

with open("inventory.txt","r") as f:
	content=f.read()
print(content)

print("Program Completed")
