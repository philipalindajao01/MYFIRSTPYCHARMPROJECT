'''

myFirstString = "Red"
mySecondString = 'My Favorite Color is'
myThirdString = 'Rimuru said \"Hello World\"!'

print(myThirdString)
print(mySecondString)
print(myFirstString)
myFirstNumber = 5

#string concantenation
print(mySecondString + " " + myFirstString)

concatResult = mySecondString + " " + myFirstString

print(concatResult)


print (myFirstString + str(myFirstNumber))

print(f'{myFirstString}{myFirstNumber}')

'''

'''
yourName = input("What is your name?")

print (f' Hi! {yourName} ')

if yourName.upper() == "JOHN":
    print ("I hate you!")
'''

'''
#THIS IS SUBSTRING:

longString = "SuperManIsStrong"
#[Start Index : End Index Excluded: STEP INTERVAL]
subString = longString[5 : 8 : 1]
print(subString)

subString = longString[5 : 8 ] #It will be automatic 1 INTERVAL
print(subString)

subString = longString[0 : 12 : 3] #Seas
print(subString)

#ReverseString
myString = "I AM FLYING"
reverseMyString = myString [::-1]
print(reverseMyString)

'''

'''
#Integer - counting numbers from (-25, 0, 100)
#int holds more than double
#Complex - if there is imaginary no. ( 25 + 25j )

a = 5
b = 25
sum = a + b
print (sum)

a = 2
b = 4
c = 3
d = 8
output = (d/b) - (a + c * d) #pmdas
print (output)

#modulo % - to get remainder

a = 55
b = 5
output = 55 % 5
print(output)

n = input("Give me your number")
if int (n) % 2 == 0:
    print ('is even')
else:
    print('is odd')

'''
a = "5"
b = "25"
sum = a + b
print (sum)

'''




'''