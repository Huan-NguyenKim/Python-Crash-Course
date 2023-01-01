'''
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:

•	 If the person is less than 2 years old, print a message that the person is
a baby.
•	 If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
•	 If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
•	 If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
•	 If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
•	 If the person is age 65 or older, print a message that the person is an
elder..
'''

# 1/ • If the person is less than 2 years old, print a message that the person is a baby.

age = 66
if age == 2:
    print("You are a baby.")


# 2/ • If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
elif age <= 4:
    print("You are a todler.")


# 3/• If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
elif age > 4 and age < 13:
    print("You are a kid")


# 4/• If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
elif age > 13 and age < 20:
    print("You are a teenager.")


# 5/• If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
elif age > 20 and age < 65:
    print("You are an adult.")

# 6/• If the person is age 65 or older, print a message that the person is an elder.
elif age >= 65:
    print("You are a senior.")

# 7/ invalid age
else:
    print("You entered an invalid age. Please type again!")