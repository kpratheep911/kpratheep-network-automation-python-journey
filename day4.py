def identify_device(hostname, os_type):
    print("\nDevice  :", hostname)
    
    if os_type == "ios":
        print("Type    : Cisco Catalyst Router")
    elif os_type == "nxos":
        print("Type    : Cisco Nexus Switch")
    elif os_type == "asa":
        print("Type    : Cisco Firewall")
    else:
        print("Type    : Unknown Device")
    
    print("-" * 35)

identify_device("R1",  "ios")
identify_device("SW1", "nxos")
identify_device("FW1", "asa")
identify_device("EX1", "junos")