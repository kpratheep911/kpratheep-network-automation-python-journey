
import os
os.system("cls")
count=0
while True:
    user_input=input("Do you need coffee yes/no?")
    count+=1
    if count ==1:
        print("why dont you try coffee. Coffee aroma will make you fresh")
    if count==2:
        print("Drnking coffee will refresh your mind")
    if count ==3:
        print("Drinking coffee will make you active")
    if count ==4:
        print("Here Coffee smell so faulous")
    if count==5:
        print(f" I asked {count} times to drink coffee. Drink coffee say yes ")
    if user_input=="yes":
        print("Nice Choice but coffee not available  Lol")
        break  
    