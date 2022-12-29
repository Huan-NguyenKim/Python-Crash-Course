'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the
change.
•	 The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.

'''

# Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.

foods = ("lobster", "sushi","salad", "soup")

#  Use a for loop to print each food the restaurant offers.
print("The buffet has 4 special foods. They are:")
for food in foods:
    print(food.title())

# •	 Try to modify one of the items, and make sure that Python rejects the change.
foods[1] = ("rice")
print("\nThe new list of foods are:")
for food in foods:
    print(food.title())
'''
Output error: 

Traceback (most recent call last):
  File "i:\Practice Computer Science\Python-Crash-Course\chapter-4\buffet.py", line 24, in <module>
    foods[1] = ("rice")
TypeError: 'tuple' object does not support item assignment
'''