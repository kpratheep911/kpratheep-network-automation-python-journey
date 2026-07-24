f = open("network_report.txt", "w")

f.write("Network Report  \n")
f.write("=============== \n")
f.write("R1-192.168.10.1 - UP \n")
f.write("R2-192.168.10.2 -DOWN\n")
f.write("SW1-192.168.10.3 -UP\n")
f.close()
print("Report Saved Successfully.......!!!!")