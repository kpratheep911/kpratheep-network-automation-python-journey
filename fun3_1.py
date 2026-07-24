def backup(ip):
    print(f"connecting to {ip}")
    config = "show run output"
    print("Backup Completed")
    return config
result=backup("192.168.10.1")
print(result)
