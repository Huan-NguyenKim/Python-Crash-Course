'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.

•	 If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
•	 If the alien’s color isn’t green, print a statement that the player just earned
10 points.
•	 Write one version of this program that runs the if block and another that
runs the else block.
'''


# •	 If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# one version of this program that runs the if block (means printing the output from IF)

alien_color1 = "red" 
print("Is the alien's color red?")
if alien_color1 == "red":
    print("Yes, the alien's color is red. You have just earned 5 points (output from IF).")
else:
    print("So sorry")

print("\n")


# If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# The program that runs the else block (means printing output from ELSE)
alien_color2 = "green"
print("Is the alien's color red?")
if alien_color2 == "red":
    print("Yes")
else:
    print("NO! The alien's color is green. You have earned 10 points (output from ELSE)")