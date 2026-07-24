devices = [
    {"hostname":"R1","ip":"192.168.10.1","vendor":"cisco","type":"IOS"},
    {"hostname":"R3","ip":"192.168.10.3","vendor":"cisco","type":"IOS"},
    {"hostname":"R2","ip":"192.168.10.2","vendor":"cisco","type":"IOS"},
    {"hostname":"R4","ip":"192.168.10.5","vendor":"cisco","type":"IOS"},
    {"hostname":"SW1","ip":"192.168.10.6","vendor":"cisco","type":"IOS"},
    {"hostname":"SW2","ip":"192.168.10.7","vendor":"cisco","type":"IOS"}
]

def check_device(hostname,ip,type):
    print("\n Device :",hostname)
    print("| IP Address :",ip)
    print("| OS Type :",type)
    print("-"*40)

print("\n MY NETWORK INVENTORY")

for device in devices :
    check_device(device["hostname"],device["ip"],device["type"])
    if device["vendor"] == "cisco":
        print("Cisco devices found",device["hostname"],device["ip"],device["vendor"],device["type"])

print("\n Total No. of devices",len(devices))