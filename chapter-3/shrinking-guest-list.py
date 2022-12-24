# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.

# 	 + Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# 	 + Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# 	 + Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# 	 + Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

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


# 	 + Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

bad_news = "\nUnfortunately, due to the inflation, I can only invite 2 friends to the party now!"
print(bad_news)

# 	 + Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

popped_friend1 = friends.pop()
bad_news1 = f"\nSorry {popped_friend1.title()}! We don't have a party anymore."
print(bad_news1)

popped_friend2 = friends.pop()
bad_news2 = f"\nSorry {popped_friend2.title()}! We don't have a party anymore."
print(bad_news2)

popped_friend3 = friends.pop()
bad_news3 = f"\nSorry {popped_friend3.title()}! We don't have a party anymore."
print(bad_news3)

popped_friend4 = friends.pop()
bad_news4 = f"\nSorry {popped_friend4.title()}! We don't have a party anymore."
print(bad_news4)


# 	 + Print a message to each of the two people still on your list, letting them
# know they’re still invited.

good_news1 = f"\nHello {friends[0].title()}! We can still have a small dinner!"
print(good_news1)

good_news2 = f"\nHello {friends[1].title()}! We can stil have a small dinner!"
print(good_news2)

# 	 + Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program. "

del friends[0]
del friends[0]

print(friends)
