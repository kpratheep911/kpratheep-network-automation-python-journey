import os
os.system("cls")
print("                             ============================================================")
print("                                Guess Game :   Can you guess my favorite cricketer")
print("                             ============================================================")
count=0
while True:
    user_input=input("                       Guess my favorite Cricket Player : ")
    count+=1
    if user_input.strip().lower()=="jadeja":
        print(f"                      Yes, Your guess is Correct. {user_input} is my favorite !!!!!!!!!")
        print(f"                                     You guessed in {count} attempts")
        break
    print(f"                                            Your guess {user_input} is wrong.Try Again")
    print("                                            ===========================================")
    if count%3==0:
        print(f" you tried {count} attempts already . Use my Hint: He won IPL cup for CSK in 2023. Especially last two balls")

