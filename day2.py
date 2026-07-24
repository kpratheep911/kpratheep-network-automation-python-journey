devices=[
    {"hostname":"R1","ip":"192.168.10.1","type":"ios"},
    {"hostname":"R2","ip":"192.168.10.2","type":"ios"},
    {"hostname":"R3","ip":"192.168.10.3","type":"ios"},
    {"hostname":"SW1","ip":"192.168.10.4","type":"nx-os"},
    {"hostname":"SW2","ip":"192.168.10.5","type":"nx-os"}
]

for device in devices:
    print("Connecting to...",device["hostname"], "| IP:",device["ip"] ,"| Type:",device["type"])
    