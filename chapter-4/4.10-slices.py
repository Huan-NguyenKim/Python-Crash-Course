# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
#   •	 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
#   •	 Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
#   •	 Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list..


#Answer
# Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:

countries = ['usa','france','vietnam','china','canada','uk','germany','brazil','australia']


#   •	 Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print("The first three countries in the list are:")
for country1 in countries[0:3]:
    print(country1.title())


#   •	 Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.
print("\nThe next three countries in the list are:")
for country2 in countries[3:6]:
    print(country2.title())




#   •	 Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.
print("\nThe last three countries in the list are:")
for country3 in countries[6:9]:
    print(country3.title())



'''Output:

The first three countries in the list are:
Usa
France
Vietnam

The next three countries in the list are:
China
Canada
Uk

The last three countries in the list are:
Germany
Brazil
Australia

'''