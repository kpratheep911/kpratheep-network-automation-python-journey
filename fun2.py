def show_ios_devices(devices):
    count =0 
    for device in devices:
        if(device["type"])=="ios" :
            count+=1
    print("Total No. of IOS devices are ",count)
devices = [
    {"hostname":"R1","ip":"1.1.1.1","type":"ios"},
    {"hostname":"R2","ip":"2.2.2.2","type":"ios"},
    {"hostname":"SW1","ip":"3.3.3.3","type":"nxos"}
]

show_ios_devices(devices)