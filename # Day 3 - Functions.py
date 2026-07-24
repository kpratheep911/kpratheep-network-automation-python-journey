# Day 3 - Functions
# The most powerful concept in Python

# WITHOUT a function - repeating yourself
print("--- Chennai Inventory ---")
print("--- Dubai Inventory ---")
print("--- London Inventory ---")

# That's 3 lines. What if you had 50 cities?
# Functions solve this.

# WITH a function - write once, use anywhere
def show_site(city):
    print("---", city, "Inventory ---")

show_site("Chennai")
show_site("Dubai")
show_site("London")
show_site("New York")
show_site("Sydney")