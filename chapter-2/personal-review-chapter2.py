'''
The purpose for this extra exercise is to review all the materials in this chapter.

'''


'''
1/ We add a variable named message. Every variable is connected to a
value, which is the information associated with that variable.Then, print that variable

'''
city = "San Francisco is a city in California"
print('1/', city)



'''2/ Naming and Using Variables
•	 Variable names can contain only letters, numbers, and underscores.
But you can call a variable message_1 but not 1_message.

•	 Spaces are not allowed in variable names, but underscores can be used
to separate words in variable names. For example, greeting_message
works, but greeting message doesn't.

•	 Avoid using Python keywords and function names as variable names. For example, keyword (print)

•	 Variable names should be short but descriptive. For example, name is
better than n, student_name is better than s_n. 

•	 Be careful when using the lowercase letter l and the uppercas

'''



'''3/ Strings

"This is a string."

'''


print('\n')


'''4/ Changing Case in a String with Methods
'''

name = 'huan nguyen'

#using title()
print('4a/ This output using name.title() method: ', name.title())


# using name.upper())
print('4b/ This output using name.upper() method: ', name.upper())


# using name.lower())
print('4c/ This output using name.lower() method: ', name.lower())



print('\n')


'''5/ Using Variables in Strings

Two variables to represent a first name and a last
name respectively. Then, combine them to display a full name
'''

first_name = 'huan'
last_name = 'nguyen'
full_name = f'{first_name} {last_name}'

print('5/ My full name is ', full_name.title())