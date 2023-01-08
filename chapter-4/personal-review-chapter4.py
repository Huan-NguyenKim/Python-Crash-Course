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