'''
5-12. Styling if statements: Review the programs you wrote in this chapter, and
make sure you styled your conditional tests appropriately
'''

# not a good style (still executable but not easily readable)
print('Can i vote?')
number=18
if number<21:
    print("Sorry! You cann't vote.")
else:
    print('Yes, you can vote') 

print('\n')

# a good style ( executable and easily readable by adding some spaces)

print("What city is in California?")

california = ['san francisco','los angeles']
cities = ['san francisco','new york']

for city in cities:
    if city in california:
        print(f'{city.title()} is in California')
    else:
        print(f'So sorry! {city.title()} is not in California.')