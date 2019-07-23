
#CHALLENGE INSTRUCTION
#Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word.
# Words will be separated by only one space.

#SOLUTION

def lettercapitalize(str):
    str = str.capitalize()
    return str

str = input("Enter your favourite word: ")
print("Your favourite word is: " + lettercapitalize(str))
