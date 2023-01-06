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


print('\n')



'''8/Removing Elements from a List

Removing an item by using the del statement.

'''

print('8a/ Removing Miami(4th item) from the list')
del cities[3]
print('8b/ The new list is: ', cities)


print('\n')



'''9/ Removing an Item Using the pop() Method

The pop() method removes the last item in a list
'''

print('9a/ Removing an item(last) using the pop method()')
new_cities =  cities.pop()
print('9b/ The city got removed is: ', new_cities)
print('9c/ The new list now is:', cities)


print('\n')



'''10/ Popping Items from any Position in a List

You can use pop() to remove an item from any position in a list by including
the index of the item you want to remove in parentheses.

'''

print('10a/ Removing the 2nd item (new york) in the list by using the pop(1) method')
cities2 = cities.pop(1)
print('10b/ The city got removed is: ', cities2)
print('10c/ The new list now is:', cities)


print('\n')



'''11/ Removing an Item by Value

 use the remove() method to remove an exact item. For example, remove(chicago)

'''

cities.remove('chicago')
print('11/ The list after removing chicago using the remove() method')


print('\n')



'''12/ Sorting a List Permanently with the sort() Method

This helps to sort a list alphabetically.

'''

alphabet = ['c', 'f', 'a', 'd', 'a']
print('12a/ The unsorted list is ', alphabet)

alphabet.sort()

print('12b/ The sorted list after using the sort() method is: ', alphabet)



print('\n')



'''13/ Sorting a List Temporarily with the sorted() Function

    The sorted() function lets you display your list
in a particular order Temporarily but doesn’t affect the actual order of the list
'''

names = ['huan', 'anh', 'dang', 'giang', 'hoang', 'liem', 'bao']
print('13a/ The original list of names is: ', names)
print('13b/ The list of names after using sorted() method (temporarily)',sorted(names))
print('13c/ The sorted() method does not affect the original list. It still is: ', names)


print('\n')



'''14/ Printing a List in Reverse Order

Use list.reverse() method

'''

print('14a/ The original list is: ', names)
names.reverse()
print('14b/ The list after using the reverse() method', names)


print('\n')



'''15/ Finding the Length of a List
len() method

'''

print('15/ The length of the list after using the len() method is', len(names))


'''16/ Avoiding Index Errors When Working with Lists

One commom type of error is while working with Lists is searching for item outsite of the range. 
For example, if your list has three items, and you ask for the fourth item, an error will display.

'''


'''Summary

    In this chapter you learned what lists are and how to work with the individual items in a list. 
    You learned how to define a list and how to add and remove elements. 
    You learned to sort lists permanently and temporarily for
display purposes. 
    You also learned how to find the length of a list and 
how to avoid index errors when you’re working with lists.
'''




'''Output

1/ The elements of the list are:  ['a', 'b', 'c']


2/ The 2nd item of the list is:  b


3/ Using list[0] to display the first item of the list, which is  a


4/ The 3rd element is C (also using title() method)


5a/ The original first city is  San Francisco
Changing the first city to los angeles
5b/ The first city of the new list is:  Los Angeles


6a/ Adding Houston as the 4th city to the list
6b/ The list now has:  ['los angeles', 'new york', 'miami', 'houston']


7a/ Inserting Chicago in the middle of the list (after newyork and before miami
7b/ The list now has:  ['los angeles', 'new york', 'chicago', 'miami', 'houston']


8a/ Removing Miami(4th item) from the list
8b/ The new list is:  ['los angeles', 'new york', 'chicago', 'houston']


9a/ Removing an item(last) using the pop method()
9b/ The city got removed is:  houston
9c/ The new list now is: ['los angeles', 'new york', 'chicago']


10a/ Removing the 2nd item (new york) in the list by using the pop(1) method
10b/ The city got removed is:  new york
10c/ The new list now is: ['los angeles', 'chicago']


11/ The list after removing chicago using the remove() method


12a/ The unsorted list is  ['c', 'f', 'a', 'd', 'a']
12b/ The sorted list after using the sort() method is:  ['a', 'a', 'c', 'd', 'f']


13a/ The original list of names is:  ['huan', 'anh', 'dang', 'giang', 'hoang', 'liem', 'bao']
13b/ The list of names after using sorted() method (temporarily) ['anh', 'bao', 'dang', 'giang', 'hoang', 'huan', 'liem']
13c/ The sorted() method does not affect the original list. It still is:  ['huan', 'anh', 'dang', 'giang', 'hoang', 'liem', 'bao']


14a/ The original list is:  ['huan', 'anh', 'dang', 'giang', 'hoang', 'liem', 'bao']
14b/ The list after using the reverse() method ['bao', 'liem', 'hoang', 'giang', 'dang', 'anh', 'huan']       


15/ The length of the list after using the len() method is 7
'''