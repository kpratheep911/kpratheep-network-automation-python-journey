import openpyxl
wb=openpyxl.Workbook()
ws=wb.active
ws.title="Network Inventory1"
ws.append([
    "Hostname",
    "IP Address",
    "Device Type",
    "Vendor",
    "Location",
    "Serial Number"
])

ws.append(["R1","10.0.0.1","Router","Cisco","Chennai","FCZ001"])
ws.append(["R2","10.0.0.2","Router","Cisco","Chennai","FCZ002"])
ws.append(["R3","10.0.0.3","Router","Cisco","Chennai","FCZ003"])
ws.append(["R4","10.0.0.4","Router","Cisco","Chennai","FCZ001"])
ws.append(["SW1","10.0.0.5","Switch","Cisco","Chennai","FCZ001"])
ws.append(["SW2","10.0.0.6","Switch","Cisco","Chennai","FCZ002"])
ws.append(["SW3","10.0.0.7","Switch","Cisco","Chennai","FCZ003"])
ws.append(["SW4","10.0.0.8","Switch","Cisco","Chennai","FCZ001"])
ws.append(["R1","20.0.0.1","Router","Cisco","Dubai","FCZ001"])
ws.append(["R2","20.0.0.2","Router","Cisco","Dubai","FCZ002"])
ws.append(["R3","20.0.0.3","Router","Cisco","Dubai","FCZ003"])
ws.append(["R4","20.0.0.4","Router","Cisco","Dubai","FCZ001"])
ws.append(["SW1","20.0.0.5","Switch","Cisco","Dubai","FCZ001"])
ws.append(["SW2","20.0.0.6","Switch","Cisco","Dubai","FCZ002"])
ws.append(["SW3","20.0.0.7","Switch","Cisco","Dubai","FCZ003"])
ws.append(["SW4","20.0.0.8","Switch","Cisco","Dubai","FCZ001"])
wb.save("Network Inventory1.xlsx")
print("Excel file created")
