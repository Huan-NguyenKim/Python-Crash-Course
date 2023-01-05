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



print('\n')



'''6/ Adding Whitespace to Strings with Tabs or Newlines
'''
print('6a/ This message does not have spaces or tabs in the beginning of the message')
print('6b/ This message has spaces and/or tabs in the beginning of the message')


print('\n')



'''7/ Stripping Whitespace

Using rstrip(), lstrip(), and strip() method. This may be helpful when comparing 2 strings
'''

name1 = ' huan '
print('7a/ Using rstrip() method', name1.rstrip())
print('7b/ Using lstrip() method', name1.lstrip())
print('7c/ Using rstrip() method', name1.strip())



print('\n')

'''8/ Avoiding Syntax Errors with Strings.

If you want to display a ' ', you should use " " in the print()
'''

print('8a/ This message will not show single quotes '' because i use single quotes for print()')
print("8b/ This message will show single quotes ' ' because i use double quotes for print()")



print('\n')


'''9/ Integers

You can add (+), subtract (-), multiply (*), and divide (/) integers in Python. 
'''

add_integer = 1 + 2
print('9a/ The result after adding integers (1 + 2) is' , add_integer)

subtract_integer = 5 - 1
print('9b/ The result after subtracting integers ( 5 - 1) is' , subtract_integer)

multiply_integer = 4 * 3
print('9c/ The result after multiplying integers (4 * 3) is ' , multiply_integer)

divide__integer = 20 / 2
print('9d/ The result after dividing integers (20 / 2) is ' , divide__integer)


print('\'n')



'''10/ Floats

Python calls any number with a decimal point a float.
'''

float1 = 0.4 + 0.2
print('The float number is (0.4 + 0.2)' , float1)


print('\n')