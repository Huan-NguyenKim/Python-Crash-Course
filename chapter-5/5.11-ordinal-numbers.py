'''
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
'''


# •	 Store the numbers 1 through 9 in a list.
numbers = ['1','2','3','4','5','6','7','8','9']

#Another way to create a list of number (in case we have to work with a much greater list such as 1-1000)
# numbers = list(range(1,9))


# •	 Loop through the list.
for number in numbers:
    if number == '1':
        print("The number is 1st.")
    elif number == '2':
        print("The number is 2nd.")
    elif number == '3':
        print("The number is 3rd.")
    else:
        print (f"The number is {number}th.")



'''Output:

The number is 1st.
The number is 2nd.
The number is 3rd.
The number is 4th.
The number is 5th.
The number is 6th.
The number is 7th.
The number is 8th.
The number is 9th.
'''


