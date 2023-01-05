# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

#creating a list called "cars", which has 5 names of different cars.
cars = ['Honda', 'Toyota', 'Mazda', 'GMC', 'Ferrari']


#creating messages, which include cars' names.
message1 = f"I would like to own a {cars[0].title()} car"
message2 = f"I would like to own a {cars[1].title()} car"
message3 = f"I would like to own a {cars[2].title()} car"
message4 = f"I would like to own a {cars[3].title()} car"
message5 = f"I would like to own a {cars[4].title()} car"

#printing the output
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)


'''Output:

I would like to own a Honda car
I would like to own a Toyota car
I would like to own a Mazda car
I would like to own a Gmc car
I would like to own a Ferrari car
'''