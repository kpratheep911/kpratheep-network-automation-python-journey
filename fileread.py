with open("animals.txt","r") as file:
    content=file.read().splitlines()
print("Animals loaded from file")
print(content)
#for animal in content:   
#print(animal)
