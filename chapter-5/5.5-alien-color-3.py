'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

•	 If the alien is green, print a message that the player earned 5 points.
•	 If the alien is yellow, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 15 points.
•	 Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''

# If the alien is green, print a message that the player earned 5 points
alien_color1 = "green"
print("Is the alien's color green?")

if alien_color1 == "green":
    print("Yes, the alien's color is green. You have just earned 5 points (Output from IF).")
elif alien_color1 == "yellow":
    print("No, the alien's color is yellow. You have earned 10 points.")
else:
    print("No. The alien's color is red. You have earned 15 points.")

print("\n")


# If the alien is yellow, print a message that the player earned 10 points.
alien_color = "yellow"
print("Is the alien's color green?")

if alien_color == "green":
    print("Yes, the alien's color is green. You have just earned 5 points.")
elif alien_color == "yellow":
    print("No, the alien's color is yellow. You have earned 10 points (Output from ELIF).")
else:
    print("No. The alien's color is red. You have earned 15 points.")