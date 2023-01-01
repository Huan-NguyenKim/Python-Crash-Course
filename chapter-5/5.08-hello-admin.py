'''
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:

•	 If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
•	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
'''

# Hello Admin: Make a list of five or more usernames, including the name
#'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:

usernames = ["huy","hoang","liem","toan","admin"]
for username in usernames:
    print("Hello",username.title())