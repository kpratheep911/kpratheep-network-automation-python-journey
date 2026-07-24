def backup(ip):
    print(f"connecting to ....{ip}")
    if ip=="10.1.1.3":
       return "failed"
    return "success"

devices=["10.1.1.1","10.1.1.2","10.1.1.3","10.1.1.4"]

success =0
failed=0

for ip in devices:
    result = backup(ip)
    if result =="success":
          success+=1
    else:
          failed+=1
print("=============Total Summary====================")
print("Total No. Of Devices : ", len(devices))
print("Success :", success)
print("Failed :", failed)