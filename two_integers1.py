def number(a,b):
    return a*b

num1=int(input("Enter your number1:"))
num2=int(input("Enter your number2:"))

result = number(num1,num2)

if result <= 1000:
    print(result)
else:
    total=num1+num2
    print(total)