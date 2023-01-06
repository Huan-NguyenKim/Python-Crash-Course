'''
The purpose for this extra exercise is to review all the materials in this chapter.

'''


'''1/ What Is a List?

A list is a collection of items in a particular order

'''

list = ['a', 'b', 'c']
print('1/ The elements of the list are: ', list)


print('\n')


'''2/ Accessing Elements in a List

    You can access any element in a list by
telling Python the position, or index
'''

print('2/ The 2nd item of the list is: ', list[1])


print('\n')



'''3/ Index Positions Start at 0, Not 1
'''

print('3/ Using list[0] to display the first item of the list, which is ', list[0])


print('\n')



'''4/ Using Individual Values from a List

You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a
value from a list.'''

print(f'4/ The 3rd element is {list[2].title()} (also using title() method)')


print('\n')



'''5/ Modifying Elements in a List

    To change an element, use the name of the list followed
by the index of the element you want to change, and then provide the new
value you want that item to have.
'''

cities = ['san francisco', 'new york', 'miami']
print('5a/ The original first city is ', cities[0].title())

print('Changing the first city to los angeles')
cities[0] = 'los angeles'
print('5b/ The first city of the new list is: ', cities[0].title())


print('\n')



'''6/ Adding/ Appending Elements to the End of a List

The simplest way to add a new element to a list is to 'append' the item to the
list. 
'''

print('6a/ Adding Houston as the 4th city to the list')

cities.append('houston')

print('6b/ The list now has: ', cities)


print('\n')



'''7/Inserting Elements into a List

You can add a new element at any position in your list by using the insert()
method.

'''

print('7a/ Inserting Chicago in the middle of the list (after newyork and before miami')
cities.insert(2 , 'chicago')
print('7b/ The list now has: ',cities)