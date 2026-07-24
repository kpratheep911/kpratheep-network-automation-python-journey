import pandas as pd
df=pd.read_excel("network_inventory.xlsx")
#print(df[["Model","IP Address","Hostname","Country"]])
print(f"{'Host_Name':<10},{'IP':<10},{'Country':<10}")
for _,row in df.iterrows():
    if row["Country"]=="India":
        print(f"Hostname:{row['Hostname']}, IP: {row['IP Address']},Country:{row["Country"]}")

