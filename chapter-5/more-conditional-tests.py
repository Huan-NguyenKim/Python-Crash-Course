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
first_name = "HUAN"
print("\nDid i type 'HUAN'? ")
print(first_name == "HUAN")

print("Did i type 'huan'?")
print(first_name.lower()=="HUAN")


print(first_name.upper())

#   3.  Using upper() method
last_name = "NGUYEN"
print("\nDid i type 'nguyen'?")
print(last_name =="nguyen")

print("\nDid i enter 'NGUYEN'?")
print(last_name.upper() =="NGUYEN")




#   4•	 Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to

# equality
number = 1
if number == 1:
    print("\nIf the number is 1, return TRUE")
else:
    print("Otherwise, return FALSE")

print("\n")

# inequality
year = 365
if year != 365:
    print("\nA year should have 365 days. You entered a wrong number. Please try again!")
else:
    print("You entered a correct number. A year has 365 days.")

print("\n")

# greater than
age = 22
if age > 21:
    print("Your age is greater than 21. You can drive a car now.")
else:
    print("Sorry you are not 21 yet! You can't drive.")

print("\n")



# less than
deposit = 500
if deposit < 10000:
    print("You don't have to report to IRS if you deposit less than 10,000 USD.")
else:
    print("If you deposit more than 10,000 USD, you will have to file form 8300 to the IRS")



# greater than or equal to
# less than or equal to


#   5•	 Tests using the and keyword and the or keyword
#   6•	 Test whether an item is in a list
#   7• 	 Test whether an item is not in a list