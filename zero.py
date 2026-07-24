
try:
    bandwidth=int(input("Enter the bandwidth"))
    users=int(input("How many users"))
    result=bandwidth/users
    print("per user",result)
except ZeroDivisionError:
    if users==0:
        print("cannot divide by zero ")
finally:
    print("Bandwidth allocation calcultion")