Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

#CHALLENGE:

# Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
# Separate the number of hours and minutes with a colon.


#SOLUTION

def timeconvert(num):
    hour = num // 60
    minutes = num - (hour * 60)
    return ':'.join([str(hour), str(minutes)])

print(timeconvert(input()))
