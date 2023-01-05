# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message should be the same, 
# but each message should be personalized with the person’s name.

#declaring a list called names, which contains all 5 names.
names = ['Huy', 'Hoang', 'Liem', 'Minh', 'Linh']

#creating 5 messages. Each message print a message with a person's name on it.
message1 = f"The first   person's name is {names[0].title()}"
message2 = f"The second  person's name is {names[1].title()}"
message3 = f"The third   person's name is {names[2].title()}"
message4 = f"The fourth  person's name is {names[3].title()}"
message5 = f"The fith    person's name is {names[4].title()}"


#printing the output
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)


'''Output:

The first   person's name is Huy
The second  person's name is Hoang
The third   person's name is Liem
The fourth  person's name is Minh
The fith    person's name is Linh
'''