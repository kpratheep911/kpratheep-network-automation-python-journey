devices =[
    "10.1.1.1",
    "10.1.1.2",
    "10.1.1.3"
]

for ip in devices :
    try:
        print(f"connecting to {ip}")
        if ip == "10.1.1.2":
            raise Exception ("Connection Timeout")
        print("connected Successfully")
    except Exception as e:
        print(f"Failed : {ip}")
        print(f"Reason : {e}")