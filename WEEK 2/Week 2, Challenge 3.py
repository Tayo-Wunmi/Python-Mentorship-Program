
#CHALLENGE:
#Given: Two positive integers a<b<10000
#Return: The sum of all odd integers from a through b inclusively. (Solve using for loops and while loops

# SOLUTION

# 1. FOR LOOP

a = 200  #assumed integer
b = 9600 #assumed integer
result = 0

for i in range(a,b+1):
  if i % 2 == 1:
    result += i
print(result)


# 2. WHILE LOOP

a = 200  #assumed integer
b = 9600 #assumed integer
result = 0

while a < b and b < 10000:
  if a % 2 == 1:
    result += a

print(result)


