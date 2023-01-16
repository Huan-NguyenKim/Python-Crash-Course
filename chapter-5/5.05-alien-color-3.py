'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

•	 If the alien is green, print a message that the player earned 5 points.
•	 If the alien is yellow, print a message that the player earned 10 points.
•	 If the alien is red, print a message that the player earned 15 points.
•	 Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''

# 1/ If the alien is green, print a message that the player earned 5 points
alien_color1 = "green"
print("Is the alien's color green? (1st program)")

if alien_color1 == "green":
    print("Yes, the alien's color is green. You have just earned 5 points (Output from IF).")
elif alien_color1 == "yellow":
    print("No, the alien's color is yellow. You have earned 10 points.")
else:
    print("No. The alien's color is red. You have earned 15 points.")

print("\n")


# 2/ If the alien is yellow, print a message that the player earned 10 points.
alien_color2 = "yellow"
print("Is the alien's color green? (2nd program)")

if alien_color2 == "green":
    print("Yes, the alien's color is green. You have just earned 5 points.")
elif alien_color2 == "yellow":
    print("No, the alien's color is yellow. You have earned 10 points (Output from ELIF).")
else:
    print("No. The alien's color is red. You have earned 15 points.")

print("\n")


# 3/ If the alien is red, print a message that the player earned 15 points.
alien_color3 = "red"
print("Is the alien's color green? (3rd program)")

if alien_color3 == "green":
    print("Yes, the alien's color is green. You have just earned 5 points.")
elif alien_color3 == "yellow":
    print("No, the alien's color is yellow. You have earned 10 points.")
else:
    print("No, the alien's color is red. You have earned 15 points. (Output from ELSE)")



'''Output:

Is the alien's color green? (1st program)
Yes, the alien's color is green. You have just earned 5 points (Output from IF).


Is the alien's color green? (2nd program)
No, the alien's color is yellow. You have earned 10 points (Output from ELIF).


Is the alien's color green? (3rd program)
No, the alien's color is red. You have earned 15 points. (Output from ELSE)

'''