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
print("\nInstering",languages[1], "to the 2nd position of the list")
print("The list now has",languages) 