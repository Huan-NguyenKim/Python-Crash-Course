# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.


# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# call to the end of your program informing people that you found a bigger dinner table.
#	+ Use insert() to add one new guest to the beginning of your list.
#	+ Use insert() to add one new guest to the middle of your list.
#	+ Use append() to add one new guest to the end of your list.
#	+ Print a new set of invitation messages, one for each person in your list.

#creating a list called "friends"
friends = ['huy', 'hoang', 'liem']

#creating the 1st set of messages
message1 = f"Would you like to join me for dinner, {friends[0].title()}?"
message2 = f"Would you like to join me for dinner, {friends[1].title()}?"
message3 = f"Would you like to join me for dinner, {friends[2].title()}?"

#Printing the 1st output
print(message1)
print(message2)
print(message3)

#making a message that 1 person can't come to the party.
NA_guest = f"\n{friends[1].title()} is not available. Hence, he won't be able to come to the party."
print(NA_guest)

#adjusting the friend list.
friends[1] = 'linh'

bigger_table = "\nWe will have a bigger table. So i would like to invite more friends."
print(bigger_table)

#   + Use insert() to add one new guest to the beginning of your list.
friends.insert(0, 'dang')

#	+ Use insert() to add one new guest to the middle of your list.
friends.insert(2, 'toan')

#	+ Use append() to add one new guest to the end of your list.
friends.append('truat')

#	+ Print a new set of invitation messages, one for each person in your list.
#creating the 2nd set of messages
message4 = f"\nWould you like to come to my party, {friends[0].title()}?"
message5 = f"Would you like to come to my party, {friends[1].title()}?"
message6 = f"Would you like to come to my party, {friends[2].title()}?"
message7 = f"Would you like to come to my party, {friends[3].title()}?"
message8 = f"Would you like to come to my party, {friends[4].title()}?"
message9 = f"Would you like to come to my party, {friends[5].title()}?"

#printing the 2nd output
print(message4)
print(message5)
print(message6)
print(message7)
print(message8)
print(message9)


length_list = len(friends)
print("\nThere are ", length_list,"friends!" " Their names are",friends)




'''Output:

Would you like to join me for dinner, Huy?
Would you like to join me for dinner, Hoang?
Would you like to join me for dinner, Liem? 

Hoang is not available. Hence, he won't be able to come to the party.

We will have a bigger table. So i would like to invite more friends.

Would you like to come to my party, Dang?
Would you like to come to my party, Huy?
Would you like to come to my party, Toan?
Would you like to come to my party, Linh?
Would you like to come to my party, Liem?
Would you like to come to my party, Truat?

There are  6 friends! Their names are ['dang', 'huy', 'toan', 'linh', 'liem', 'truat']
'''