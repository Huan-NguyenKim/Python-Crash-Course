'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

•	 Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
•	 Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.

'''

# Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
alien_color1 = "green"
if alien_color1 == "green":
    print("The alien is gree. You have just earned 5 points!")
else:
    print("So sorry!")


#  another that fails. (The version that fails will have no output.
alien_color2 = "red"
if alien_color2 == "green":
    print("\nIs the alien's color green?")


'''Output:

The alien is green. You have just earned 5 points!
'''