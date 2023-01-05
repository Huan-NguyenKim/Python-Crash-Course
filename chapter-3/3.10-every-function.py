# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

languages = ['English','Cantonese','Vietnamese','Mandarin','Spanish']

#printing the original list
print("\nThe original list is",languages)

#Accessing Elements in a List
#Using Individual Values from a List
#printing the element in the 3rd position
print("\nThe 3rd language on the list is",languages[2])


#Modifying Elements in a List
languages[4] = "German"
print("\nReplacing Spanish with",languages[4])

#Appending Elements to the End of a List
languages.append("French")
print("\nAdding French to the end of the list. The list of languages now contain", languages)

#Inserting Elements into a List
languages.insert(1,"Japanese")
print("\nInstering",languages[1], "to the 2nd position of the list.")
print("The list now has",languages) 

#Removing an Item Using the del Statement
del languages[2]
print("\nRemoving the 3rd language, which is Cantonese.")
print("The list now has",languages)

#Removing an Item Using the pop() Method. This is to remove the last item in the list
popped_language = languages.pop()
print("\nThe popped item is",popped_language)
print("The new list after using the pop() method is", languages)


# Popping Items from any Position in a List
another_popped_language = languages.pop(0)
print("\nAnother popped language is",another_popped_language)
print("The language list now has",languages)

#Removing an Item by Value. This means removing an item by its name even though we don't know its position.
languages.remove("Mandarin")
print("\nRemoving Mandarin from the list")
print("The list now is",languages)

#Sorting a List Temporarily with the sorted() Function
print("\nThe temporary sorted list of language is",sorted(languages))

#Printing the original list
print("\nThe original list is still", languages)

#Sorting a List Permanently with the sort() Method
languages.sort()
print("\nThe list is now permanently sorted, which include", languages)

#Printing a List in Reverse Order
languages.reverse()
print("\nThe reverse order is ",languages)


#Finding the Length of the list
list_length = len(languages)
print("\nThe length of the list is", list_length)



'''Output:

The original list is ['English', 'Cantonese', 'Vietnamese', 'Mandarin', 'Spanish']

The 3rd language on the list is Vietnamese

Replacing Spanish with German

Adding French to the end of the list. The list of languages now contain ['English', 'Cantonese', 'Vietnamese', 'Mandarin', 'German', 'French']

Instering Japanese to the 2nd position of the list.
The list now has ['English', 'Japanese', 'Cantonese', 'Vietnamese', 'Mandarin', 'German', 'French']

Removing the 3rd language, which is Cantonese.
The list now has ['English', 'Japanese', 'Vietnamese', 'Mandarin', 'German', 'French']

The popped item is French
The new list after using the pop() method is ['English', 'Japanese', 'Vietnamese', 'Mandarin', 'German']      

Another popped language is English
The language list now has ['Japanese', 'Vietnamese', 'Mandarin', 'German']

Removing Mandarin from the list
The list now is ['Japanese', 'Vietnamese', 'German']

The temporary sorted list of language is ['German', 'Japanese', 'Vietnamese']

The original list is still ['Japanese', 'Vietnamese', 'German']

The list is now permanently sorted, which include ['German', 'Japanese', 'Vietnamese']

The reverse order is  ['Vietnamese', 'Japanese', 'German']
The length of the list is 3
'''
