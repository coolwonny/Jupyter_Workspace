# Create a grocery list for the apple pie ingredients:
grocery = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]

# Water
# Butter
# Eggs
# Apples
# Cinnamon
# Sugar
# Milk

# Find the first two items on Mike's grocery list.
print(grocery[:2])

# Find the last five items on Mike's grocery list.
print(grocery[-5:])
# Find every other item, starting from the second item, on Mike's grocery list.
print(grocery[1::2])
# Add flour to the grocery list.
grocery.append("Flour")
print(grocery)
# Change apples to gala apples. (Mike decides to be more specific with the types of apples needed.)
grocery[3] = "Gala Apples"
print(grocery)
# Determine the total number of items on the grocery list.
print(len(grocery))

#Challenge
# Mike arrives at the supermarket and walks through the aisles 
# to gather the items on the list. Help him with the following tasks.
# Mike wants to find where gala apples is on his list.
#  Find the index of gala apples.
print(grocery.index("Gala Apples"))
# Mike remembers that he already has sugar. 
# Remove sugar from the grocery list.
grocery.remove("Sugar")
print(grocery)

# Mike decides that he has water at home. 
# Remove water from the grocery list based on its index.
del grocery[0]
print(grocery)

# Mike decides to pick up the last item on his list, 
# so remove the last item from the grocery list.
grocery.pop()
print(grocery)