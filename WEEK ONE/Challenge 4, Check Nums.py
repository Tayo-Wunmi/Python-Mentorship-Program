Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #CHALLENGE:

# Have the function CheckNums(num1,num2) take both parameters being passed and return the string true if num2 is greater than num1,
# otherwise return the string false.
# If the parameter values are equal to each other then return the string -1.

#SOLUTION
def checknums(num1, num2):
    if num2 > num1:
        return 'true'
    elif num2 == num1:
        return '-1'
    else:
        return 'false'

    return checknums()

print(checknums(7, 5))
