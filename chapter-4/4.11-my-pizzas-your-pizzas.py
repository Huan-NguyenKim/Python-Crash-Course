 # 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
#   •	 Add a new pizza to the original list.
#   •	 Add a different pizza to the list friend_pizzas.
#   •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list..


# From 4.1 practice:
# Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza

pizzas = ['pizza1','pizza2','pizza3']
for pizza in pizzas:
    print("\n",pizza)


#   •	 Modify your for loop to print a sentence using the name of the pizza
#   instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni pizza.
    print(f"\nI really like {pizza.title()}")


#   •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
print("\nI love all kinds of pizzas")


# Make a copy of the list of pizzas, and call it friend_pizzas.
friend_pizzas = pizzas[:]
print("\nFriend_pizzas is a copied list of the pizzas list. It contains",friend_pizzas)


#   •	 Add a new pizza to the original list.
pizzas.append("pizza4")



#   •	 Add a different pizza to the list friend_pizzas.
friend_pizzas.append("new pizza")

#   •	 Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.


print("\nThe original list now has 4 items. They are:")
for pizza in pizzas[:]:
    print(pizza.title())


print("\nThe friend_pizzas list now has 4 items too. They are:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza.title())