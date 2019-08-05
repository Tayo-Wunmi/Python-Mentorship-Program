Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 

#CHALLENGE:
#Write a short program that prints the numbers 1 to 10 using a for loop.
# Then write an equivalent program that prints the numbers 10 to 1 using a while loop.

#SOLUTION

# 1. FOR LOOP
for i in range(1,11):
    print(i)


# 2. WHILE LOOP

number = 1
while number <= 10:
    print(number)
    number += 1
