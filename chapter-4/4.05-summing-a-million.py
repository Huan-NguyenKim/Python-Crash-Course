# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers..

numbers = list(range(1,1000001))

print('The min is', min(numbers))
print('The max is', max(numbers))
print('The sum is', sum(numbers))



'''Output:

The min is 1
The max is 1000000
The sum is 500000500000

'''