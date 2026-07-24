devices =[
    "10.1.1.1",
    "10.1.1.2",
    "10.1.1.3"
]
success=[]
failed=[]
for ip in devices :
    try :
        print(f"connecting to ...{ip}")
        if ip == "10.1.1.2":
            raise Exception("Connection Timeout")
        print(f"Connected Successfully")
        success.append(ip)

    except Exception as e:
        print(f" Failed : {ip}")
        print(f" Reason : {e}")
        failed.append(ip)
print("\n" + "=" *40)
print("*" *40)
print(f"Success  : {len(success)}")
print(f"Failed   : {len(failed)}")
print("*" *40)
print("=" * 40)
