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