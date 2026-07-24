def backup(ip):
    print(f"connecting to {ip}")
    print("-"*40)
    print(f"Taking Backup {ip}")
    print(f"{ip} Backup job completed")

devices =[
    "10.1.1.1","10.1.1.2","10.1.1.3"
]

for ip in devices :
    backup(ip)
    