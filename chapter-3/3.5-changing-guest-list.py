# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
#   + Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# 	+ Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
#   + Print a second set of invitation messages, one for each person who is still in your list

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

#creating messages
message4 = f"\nWould you like to come to my party, {friends[0].title()}?"
message5 = f"Would you like to come to my party, {friends[1].title()}?"
message6 = f"Would you like to come to my party, {friends[2].title()}?"

#printing the output
print(message4)
print(message5)
print(message6)