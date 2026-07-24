import pandas as pd
df=pd.read_excel("network_inventory.xlsx")
print(f"{df.columns[0]:<14} {df.columns[1]:<14}")
print("-"*40)
for index, row in df.iterrows():
    print(f'{row["Hostname"]:<14} {row["IP Address"]:<14}')
   