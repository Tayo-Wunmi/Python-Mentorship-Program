# CHALLENGE 2

#Instruction: 
#Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
#For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

#Solution 1

def firstreverse(str):
    fav_word = ""
    for x in str:
        fav_word = x + fav_word
    return fav_word

str = input("Enter your favourite word: ") 
print("The reverse of your favourite word is: " + firstreverse(str))


#Solution 2

def firstreverse(str):
    str = str[::-1]
    return str

str = input("Enter your favourite word: ")
print("The reverse of your favourite word is: " + firstreverse(str))
