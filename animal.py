with open("animals.txt","w") as file:
    file.write("Lion\n")

with open("animals.txt","a") as file:
    file.write("Tiger\n")
    file.write("Jackal\n")
    file.write("fox\n")

with open("animals.txt","r") as file:
    animal=file.read()
    print(animal)