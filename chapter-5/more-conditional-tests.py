'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
•	 Tests for equality and inequality with strings
•	 Tests using the lower() method
•	 Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
•	 Tests using the and keyword and the or keyword
•	 Test whether an item is in a list
•	 Test whether an item is not in a list

'''

#   1•	 Tests for equality and inequality with strings
#a/ equality

mobile_phone = "samsung"
print("Samsung has a new model right now. Do you want to buy one? (checking for equality)")
if mobile_phone == "samsung":
    print("I love Samsung phones. I will buy one")
else:
    print("I don't want to buy other phones.")

print("\n")


#b/ inequality
favorite_food = "noodles"
print("Are you hungry? But we don't have noodles right now (checking for inequality)")
if favorite_food != "noodles":
    print("I don't want to eat right now.")
else:
    print("I will wait for noodles later.")


#   2•	 Tests using the lower() method
name = "HUAN"
print("\nDid i type 'HUAN'? ")
print(name == "HUAN")

print("Did i type 'huan'?")
print(name.lower()=="HUAN")


#   3•	 Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
#   4•	 Tests using the and keyword and the or keyword
#   5•	 Test whether an item is in a list
#   6• 	 Test whether an item is not in a list