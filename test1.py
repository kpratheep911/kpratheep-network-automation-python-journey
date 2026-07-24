def backup(ip):
    print(f"connecting to ...{ip}")
    print("Backup completed")
    
devices =[
    "10.1.1.1","10.1.1.2","10.1.1.3","10.1.1.4"
]
success=0
for ip in devices :
    backup(ip)
    success+=1
print("=====Summary======")
print("Total devices",len(devices))
print("Success",success)    
