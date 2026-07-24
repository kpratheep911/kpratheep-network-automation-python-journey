try:
    file = open("devices123.txt", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("Devices file is missing")

finally:
    print("Execution completed")