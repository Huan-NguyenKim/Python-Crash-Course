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

# " " and ' ' are similar..
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

#3 languages (also using upper case to compare to the original lower case.)
language = "english"
print("\nIs the language 'english'?")
print(language == "english")

print("Is the language 'vietnamese'?")
print(language =="vietnamese")

print("The language is english but the return result will be false because using ENGLISH to test.")
print(language =="ENGLISH")


#4 holidays (also using lower case to compare to the original upper case.)
holiday = "NEW YEAR"
print("\nIs the holiday 'NEW YEAR' (upper case)?")
print(holiday == "NEW YEAR")

print("Is the holiday 'new year' (lower case)?")
print(holiday == "new year")


#5 currencies (also checking whether or not 'space' (from no space to space) would make a difference)
currency1 = "usd"
print("\nIs the currency 'usd'?")
print(currency1 == "usd")

print("Is the currency still 'usd' (u s d)?")
print(currency1 == "u s d")


#6 similar to #5 but checking from "space to no space"
currency2 = "u s d"
print("\nIs the currency 'u s d' (space)?")
print(currency2 == "u s d")

print("Is the currency 'usd' (no space)?")
print(currency2 == "usd")



'''Output:

Is the city 'San Francsico'?
True
Is the city 'New York'?
False

Is the country 'usa'?
True
Is the country 'vietnam'?
False

Is the language 'english'?
True
Is the language 'vietnamese'?
False
The language is english but the return result will be false because using ENGLISH to test.
False

Is the holiday 'NEW YEAR' (upper case)?
True
Is the holiday 'new year' (lower case)?
False

Is the currency 'usd'?
True
Is the currency still 'usd' (u s d)?
False

Is the currency 'u s d' (space)?
True
Is the currency 'usd' (no space)?
False

'''