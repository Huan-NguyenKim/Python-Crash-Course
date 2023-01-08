'''
The purpose for this extra exercise is to review all the materials in this chapter.

'''


'''1/ For Looping

    Python prints the current value of list. Then,Python repeats the entire loop 
until the last value in the list.
    If there is no more values in the list, the program simply ends.

'''

cities = ['san francisco', 'los angeles', 'hayward']
for city in cities:
    print(f'1/ {city.title()} is a city in California')


print('\n')



'''2/ Doing Something After a for Loop

    Any lines of code after the for loop that are not indented are executed
once without repetition.
'''

cities2 = ['new york', 'houston', 'miami']
for city2 in cities2:
    print(f'2a/ {city2.title()} is city outside of California.')

print('\n2b/ These cities are not in California (this statement is outside of the loop)')


print('\n')



'''3/ Avoiding Indentation Errors

If you don't indent(space) for the 2nd line after the FOR loop, an error will occur.

'''

print('3/ We have to remember to indent(space) for the 2nd line after te FOR loop to avoid errors.')


'''
Example of not indenting

cities2 = ['new york', 'houston', 'miami']
for city2 in cities2:
print(f'2a/ {city2.title()} is city outside of California.')

Output: This will cause an error.
'''


print('\n')



'''4/ Indenting Unnecessarily After the Loop

If PRINT() is not a part of the FOR loop, we don't have to indent

'''

print("4/ If PRINT() is not a part of the FOR loop, we don't have to indent")


'''
Example of indenting unnecessarily


cities2 = ['new york', 'houston', 'miami']
for city2 in cities2:
    print(f'2a/ {city2.title()} is city outside of California.')
    print('\n2b/ These cities are not in California (this statement is outside of the loop)')

#The above print() is not inside a loop, so we don't need to indent.

Output: This will cause an error.
'''

print('\n')



'''5/ Making Numerical Lists

Python’s range() function makes it easy to generate a series of numbers. 

'''
print('5/ Please note that if a range 1 to 6, the system only displays 1 to 5')
for number in range(1, 6):
    print('For example', number , 'is the number in range from 1 to 6')


print('\n')


'''6/ Using range() to Make a List of Numbers

    If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers.
'''

numbers = list(range(6, 10))
print('6/ The list of numbers from range 6 to 10 are: ', numbers)


print('\n')


'''7/ We can also use the range() function to tell Python to skip numbers in a
given range

For example, we can use range() to create a list of EVEN NUMBERS
'''

even_numbers = list(range(2, 11, 2)) 
# This means we start from 2, then add 2 until the last number of the list, which is 11

print('7/ The list of even numbers from 2 to 11 are:', even_numbers)


print('\n')



'''8/ Similarly, we can use range() to create a list of ODD NUMBERS

'''

odd_numbers = list(range(1, 11, 2))
# This means we start from 1, then add 2 until the last number of the list, which is 11

print('8/ The list of odd numbers from 1 to 11 are:', odd_numbers)

print('\n')



'''9/ We can do this method to do calculations as well. But it is a little bit more complicated.

For example, we try to find the multiples of 3.
'''

multiples_of_3 = []     #create an empty list

integers = list(range(1, 11))           #a list of integers from 1 to 11
for integer in integers:                #for loop
    multiples_of_3.append(integer * 3)  #adding values (*3) to each integer (1 to 11)

print('9/ The multiples of 3 (from 1 to 11) are:', multiples_of_3)    #output