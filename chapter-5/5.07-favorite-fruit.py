'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.

•	 Make a list of your three favorite fruits and call it favorite_fruits.
•	 Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
'''

# •	 Make a list of your three favorite fruits and call it favorite_fruits.
favorite_fruits = ["apple","avocado","durian","cherry","kiwi"]


# Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!
if "apple" in favorite_fruits:
    print("I love apples!")

if "avocado" in favorite_fruits:
    print("\nI love avocados!")

if "durian" in favorite_fruits:
    print("\nI love durians!")

if "cherry"  in favorite_fruits:
    print("\nI love cherries!")

if "kiwi" in favorite_fruits:
    print("\nI love kiwis!")

if "banana" not in favorite_fruits:
    print("\nSorry banana is not on the list.")

print("\nDo you like fruits?")