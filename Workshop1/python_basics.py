"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """

    num = int(input("Enter number: "))
    if num % 2 == 0:
    	print("even")
    else:
    	print("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    finish = False
    num = random.randrange(1, 9)
    while finish == False:
    	yesexit = input("Enter guess ")
    	if yesexit == "exit":
    		break
    	guess = int(yesexit)
    	if guess == num:
    		print("Exactly right")
    	elif (guess < num):
    		print("Too low")
    	elif (guess > num):
    		print("Too high")



def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """

   	dummy = string(input("enter string "))

   	for i in xrange(0, len(dummy)/2):
   		if(dummy[i] != dummy[len(dummy) - i - 1]:
   			print("not palindrome")

   	print(palindrome)


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    encodedUser = base64.b64encode(username)
    encodedPass = base64.b64encode(password)

    with open(filename) as file:
    	file.write(encodedUser)
    	file.write("\n")
    	file.write(encodedPass)

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """

    with open(filename) as file:
    	info = file.read
    	username = base64.b64decode(info[0])
    	password = base64.b64decode(info[1])
    	print(username + " " + password)
    	if(password):
    		newPasEncode = base64.b64encode(password)
    		info[1] = newPasEncode
    		file.write(info)


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
