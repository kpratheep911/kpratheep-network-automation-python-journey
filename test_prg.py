devices = [
    {"hostname": "R1", "vendor": "Cisco", "ip": "10.1.1.1"},
    {"hostname": "R2", "vendor": "Juniper", "ip": "10.1.1.2"},
    {"hostname": "R3", "vendor": "Cisco", "ip": "10.1.1.3"}
]

def Dev_ip():
   for device in devices:
      if(device["vendor"]) =="Cisco":
	        print(f"{device['vendor']} device ip is {device['ip']}")

Dev_ip()
