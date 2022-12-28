# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes = []                           # initializing cubes
for value in range(1,11):            # range from 1 to 11. The program will use all numbers from 1 to 10
    cube_value = value**3            # cube is **3 (ex 1^3)
    cubes.append(cube_value)         # add all cube values to the list "cubes"
print(cubes)                         # print output