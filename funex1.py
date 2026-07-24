def router():
    routers=["cisco","juniper","Aruba"]
    for router in routers:
         print(router)

def switch():
     switches=["cisco_catalyst","cisco_nexus","cisco_leaf","cisco_spines"]
     for switch in switches :
          print("\n The Cisco switches :",switch)

router()
switch()
