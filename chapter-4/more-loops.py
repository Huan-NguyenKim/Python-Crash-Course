"""
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

"""



'''
Original program from the book (page 63)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

'''

my_foods = ['pizza', 'falafel', 'carrot cake']
print("My favorite foods are:")
for my_food in my_foods[:]:
    print(my_food.title())




friend_foods = my_foods[:]

