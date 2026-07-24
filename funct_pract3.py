def check_ip(ip):
    if ip.startswith("10."):
        print(f"{ip} - private ip ")
    else:
        print(f"{ip} - public ip  ")
check_ip("10.1.1.1")
check_ip("1.1.1.1")