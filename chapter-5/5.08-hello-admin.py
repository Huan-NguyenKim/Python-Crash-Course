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



# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Jaden, thank you for
# logging in again.

for username in usernames:   #this will be used to return the names.
    if username == "admin":  #checking whether or not "ADMIN" is in the list. Then, return a special output
        print(f"Hello {username.title()}! Would you like to see a report?")
    else:
        print(f"Hello {username.title()}! Thank you for logging in!")
    


   
