# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cubes = [value**3 for value in range(1,11)]
print('The list of the first 10 cubes (1 to 10) are', cubes)


'''Output:

The list of the first 10 cubes (1 to 10) are [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

'''