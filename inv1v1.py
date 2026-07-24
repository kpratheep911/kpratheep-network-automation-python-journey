import openpyxl 
def load_inventory(filename):
    devices=[]
    wb=openpyxl.load_workbook(filename)
    ws=wb.active
    for row in ws.iter_rows(min_row=2,values_only=True):
        device={
            "hostname":row[0],
            "ip"      :row[1],
            "dev_type":row[2],
            "Vendor"  :row[3],
            "location":row[4],
            "serial"  :row[5],
        }
        devices.append(device)
    return devices
def show_all(devices):
    print("\n"+"="*50)
    print(f"{'hostname':<14} {'IP':<14} {'Type':<14} {'Location':<14} {'Serial':<10}")
    print("\n"+"="*50)
    for device in devices:
        print(f"{str(device['hostname']):<14}"
              f"{str(device['ip']):<14}"
              f"{str(device['dev_type']):<14}"
              f"{str(device['location']):<14}"
              f"{str(device['serial']):<14}")
        print("="*50)
        print(f"Total :{len(devices)} devices")
       
devices=load_inventory("network_inventory.xlsx")
print(f"Inventory Loaded : {len(devices)}devices")

print("\n Search by :")
print("1.Hostname")
print("2.IP Address")
print("3.Device Type")
print("4.Location")
print("5.Show All")

choice = input("Enter choice (1-5)")

if choice =="1":
    search=input("Enter hostname")
    field="hostname"
elif choice=="2":
    search=input("Enter IP Address")
    field="ip"
elif choice=="3":
    search=input("Enter Device Type")
    field="dev_type"
elif choice=="4":
    search=input("Enter Location")
    field="location"
elif choice=="5":
      show_all(devices)
if choice!="5":
    found = False

for device in devices:
    if str(device[field]).lower()==search.lower():
        print("=*50")
        print(f"{search} is found ")
        print("="*50)
        print(f"Hostname  :{device['hostname']}")
        print(f"IP        :{device['ip']}")
        print(f"Type      :{device['dev_type']}")
        print(f"Location  :{device['location']}")
        print(f"Country   :{device['country']}")
        print(f"Serial    :{device['serial']}")
        print("="*50)
        found=True
if not found:
        print("Your search not found, Try with different value! \n Thank You")