#2-7. Stripping Names: Use a variable to represent a person’s name, and include
#some whitespace characters at the beginning and end of the name. Make sure
#you use each character combination, "\t" and "\n", at least once.

#Print the name once, so the whitespace around the name is displayed.
#Then print the name using each of the three stripping functions, lstrip(),
#rstrip(), and strip().

name = "\tHuan Nguyen\n"
print("\nNot using any methods")
print(name)

print("\nUsing the lstrip method")
print(name.lstrip())

print("\nUsing the rstrip method")
print(name.rstrip())

print("\nUsing the strip method")
print(name.strip())



'''Output

Not using any methods
        Huan Nguyen


Using the lstrip method
Huan Nguyen


Using the rstrip method
        Huan Nguyen

Using the strip method
Huan Nguyen

'''