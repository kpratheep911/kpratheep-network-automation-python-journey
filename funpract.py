def backup(ip):

    if ip == "10.1.1.3":
        return "Failed"
    return "Success"
print(backup("10.1.1.1"))
print(backup("10.1.1.3"))
