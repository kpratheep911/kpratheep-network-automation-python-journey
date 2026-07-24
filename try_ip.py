

try:
    ip=input("Enter the IP_Address")
    octets=ip.split(".")
    if (len(octets)!=4):
        print("invalid ip address")
    for octet in octets:
        if not octet.isdigit() or int(octet)<0 or int(octet)>255:
            print("Invalid IP")
    print("Valid IP Address")

except:
    print("Incorrect IP")
finally:
    print("Program Executes correct")