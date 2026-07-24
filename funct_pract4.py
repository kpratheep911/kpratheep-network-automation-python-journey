def add_device(devices,device):
    devices.append(device)
    return devices

devices=[]
devices=add_device(devices,"sw1")
devices=add_device(devices,"sw2")
print(devices)

def search(devices,search):
    found=False
    for device in devices:
        if device==search:
            found=True
            print("device found")
        if not found:
            print("Device not found")
search(devices,"sw1")
