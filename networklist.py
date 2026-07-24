with open("network_inventory.xlsx","r") as file:
    inventory=file.read()
print(" Network Inventory List")

for list in inventory:
    print(list)