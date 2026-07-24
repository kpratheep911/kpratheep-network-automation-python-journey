import pandas as pd
import os
os.system=("clear")
df=pd.read_excel("sample_inventory.xlsx")
#print(df[["Hostname","IP Address","Site Location","Country"]])
countries=sorted(df["Country"].dropna().unique())
for index,country in enumerate(countries,start=1):
    print(index,country)

choice=int(input("Choose your Country[1-10] :"))
#for i in range(1,11):
    #if i == choice:
selected_country=countries[choice-1]
print(f"Your selected country is {selected_country}\n\nFind {selected_country} locations below :")

country_df=df[df["Country"]==selected_country]
locations=sorted(country_df["Site Location"].dropna().unique())
for index, location in enumerate(locations, start=1):
    print(index, location)
location_choice=int(input("Choose your Location :"))
selected_location=locations[location_choice-1]
print(f"Your selected Location is {selected_location}\n\n Find the location Devices below:")
device_df=country_df[country_df["Site Location"]==selected_location]


for i,(_,row) in enumerate(device_df.iterrows(),start=1):
    print(f"{i}.{row['Hostname']:<20}||{row['IP Address']:<15}||{row['Site Location']:<15}||{row['Role']:<25}||")
print("=" * 88)
print(f"Location: {selected_location} - Devices Listed here")
print(f"Total Devices : {len(device_df)} ")
print("=" * 88)

device_choice=int(input("Select your Device : "))
selected_device=device_df.iloc[device_choice-1]
print(f"Selected device :{selected_device['Hostname']}")
print(f"IP Address :{selected_device['IP Address']}")
print(f"Site Location :{selected_device['Site Location']}")
print(f"Role :{selected_device['Role']}")




    