devices=[
    {"hostname":"R1","ip":"1.1.1.1","type":"ios"},
    {"hostname":"R2","ip":"2.2.2.2","type":"ios"},
    {"hostname":"R3","ip":"3.3.3.3","type":"ios"},
    {"hostname":"SW1","ip":"4.4.4.4","type":"nxos"},
    {"hostname":"sw2","ip":"5.5.5.5","type":"nxos"}
]

for device in devices:
    if device["type"]=="ios":
        print("Device found:",device["hostname"]," | IP :",device["ip"])

