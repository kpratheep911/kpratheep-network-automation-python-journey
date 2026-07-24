import os
os.system("cls")
messages=[
    "Hey, Do you need coffee",
    "Drink Coffeee, You will enjoy this Morning",
    "Its Excellent Aroma, Try this coffee",
    "why dont you try coffee. Coffee aroma will make you fresh",
    "Drnking coffee will refresh your mind",
    "Drinking coffee will make you active",
    "Here Coffee smell so faulous",
]

count=0
while True:
    user_input=input("Do you need coffee ?[yes/No]: ")
    if count<=len(messages):
        print(messages[count-1])
    if len(messages)==0:
        print(f"Asked {count} times to drink coffee. Say yes to coffee... You dont have other option")
    if user_input == "yes":
        print("Nice Choice, But It is Tea Shop Lol \U0001F923")
        break
