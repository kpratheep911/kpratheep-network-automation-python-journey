f =open("network.txt","w")

f.write("Exxon Mobil Network Report\n")
f.write("=============================\n")
f.write("Router1-192.168.10.1-UP\n")
f.write("Router2-192.168.10.2 -DOWN\n")
f.write("SW1-192.168.10.3-UP\n")
f.close()
print("Report saved!!!!!!!!")