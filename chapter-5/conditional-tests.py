'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:


car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


•	 Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•	 Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.

'''

# " " and ' ' are similar.
#1 cities
city = 'san francisco'
print("Is the city 'San Francsico'?")
print(city=='san francisco')

print("Is the city 'New York'?")
print(city=='new york')


#2 countries
country = "usa"
print("\nIs the country 'usa'?")
print(country =='usa')

print("Is the country 'vietnam'?")
print(country=='vietnam')

#3 languages (also lower case and upper case)
language = "english"
print("\nIs the language 'english'?")
print(language == "english")

print("Is the language 'vietnamese'?")
print(language =="vietnamese")

print("The language is english but the return result will be false because using ENGLISH to test.")
print(language =="ENGLISH")