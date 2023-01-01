'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.

•	 If the list is empty, print the message We need to find some users!
•	 Remove all of the usernames from your list, and make sure the correct
message is printed.
'''

#Creating an empty list
usernames = []


# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.
if 

for username in usernames:   #this will be used to return the names.
    if username == "admin":  #checking whether or not "ADMIN" is in the list. Then, return a special output
        print(f"Hello {username.title()}! Would you like to see a report?")
    else:
        print(f"Hello {username.title()}! Thank you for logging in!")