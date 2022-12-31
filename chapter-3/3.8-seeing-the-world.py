# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#   •Store the locations in a list. Make sure the list is not in alphabetical order.
#   •Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
#   •Use sorted() to print your list in alphabetical order without modifying the actual list.
#   •Show that your list is still in its original order by printing it.
#   •Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#   •Show that your list is still in its original order by printing it again.
#   •Use reverse() to change the order of your list. Print the list to show that it order has changed.
#   •Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#   •Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#   •Use sort() to change your list so it’s stored in reverse alphabetical order.
#   Print the list to show that its order has changed.



#   •Store the locations in a list. Make sure the list is not in alphabetical order.
places = ['France', 'Uk', 'Germany', 'China', 'Australia']



#   •Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
print("\nThe original list is" , places)


#   •Use sorted() to print your list in alphabetical order without modifying the actual list.
sorted_list = sorted(places)
print("\nThe temporary sorted list is",sorted_list)


#   •Show that your list is still in its original order by printing it again.
print("\nThe original list is still",places)


#   •Use reverse() to change the order of your list. Print the list to show that it order has changed.
places.reverse()
print("\nThe reversed list is",places)


#   •Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print("\nThe reversed list is reversed back to the original list again",places)


#   •Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print("\nThe permanently sorted list is",places)


#   •Use sort() to change your list so it’s stored in reverse alphabetical order.
places.sort(reverse=True)

#   Print the list to show that its order has changed.
print("\nThe list is reversed again",places)
