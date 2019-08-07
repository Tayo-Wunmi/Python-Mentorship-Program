
# CHALLENGE 
#Write a program that simulates rolling a die. When the program runs, it will randomly choose a number between 1 and 6 and print,
#then ask the user if they will like to roll again.


# SOLUTION 
print("Welcome to the Dicing Game. Lets roll!")
dice = input("Will you like to Roll your dice:  ")

import random
min = 1
max = 6

dice = "yes"
roll_again = "yes"

while dice=="yes" or roll_again=="yes":
    print("Roll! Roll! Roll")
    print("Your Lucky Number is.........")
    print(random.randint(min, max))

    if roll_again == "no":
        print("Thank you Dicer")

    break

roll_again = input("Will you like to Roll your dice again:  ")

