# 3-11. Intentional Error: If you haven’t received an index error in one of your
# programs yet, try to make one happen. 
# Change an index in one of your programs to produce an index error. 
# Make sure you correct the error before closing the program.

list = ["hi", "hello","greetings","ni hao"]
#print("Showing an index error", list[10])
#This will show an index error because the list only has 4 items. It cann't return the 10th value as we want.

print('a/ It shows an eror because the list only has 4 items but we use list[10]')



# Correct way to use list
print("b/ Showing the correct list", list)



'''Output:

a/ It shows an eror because the list only has 4 items but we use list[10]
b/ Showing the correct list ['hi', 'hello', 'greetings', 'ni hao']
'''