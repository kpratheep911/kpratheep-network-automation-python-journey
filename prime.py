num1=int(input("Enter your number1"))
while True:
    if num1<=1:
        print("Enter greater than 1")
        break
    elif num1==2:
        print(f"{num1} is prime")
        break

    for i in range(2,num1):
        if num1%i==0:
            print(f"{num1} is not a prime")
        break
    
    else:
        print(f"{num1} is prime")
        break