def number(a,b):
    return a*b

num1=int(input("Enter your number1:"))
num2=int(input("Enter your number2:"))

result = number(num1*num2)
#print("The product of two numbers:",result)
sum=number(num1+num2)
#print("The sum of two numbers are :",sum)

if result <= 1000:
    print(result)
else:
    print(sum)