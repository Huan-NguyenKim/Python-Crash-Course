# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, 
# and then use a for loop to print out the name of each animal.
#   •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
#   •	 Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!!


#Answer

# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.

pets = ['dog','cat','bird']
for pet in pets:
    print("\n", pet)


#   •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.

    print(f"\n{pet.title()} would be a great pet")


#   •	 Add a line at the end of your program stating what these animals have inn
# common. You could print a sentence such as Any of these animals would
# make a great pet!
print(f"\nMany people love {pet.title()}")



'''Output:

 dog

Dog would be a great pet

 cat

Cat would be a great pet

 bird

Bird would be a great pet

Many people love Bird

'''