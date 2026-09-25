
'''
#float
#complex number
a = 25.5
b = 13.27
prod = a * b
print(prod)
a = 10
b = 3
qout = a / b
print(qout)
print (round(qout, 2)) # round off
#complex: (25 - 25j) (10 - 10j) = 250 - 250j - 250j +250(-1) = -500j
a = 25 - 25j
b = 10 - 10j
c = a * b
print (c)

import math
a = 5
b = 25
c = math.remainder(b, a)
print(c)
c = math.factorial(a)
print(c)
c = math.log(a)
print(c)

'''


'''
#Boolean - True 1 or Fale 0
#True not "True" not true
#False not "False" not false

#Comparison Operator
# > greater than, < less than
# >= or <=
# == equal or != not equal
'''
a = 5
b = 7
print (a <= b)
isCorrect = a == b
print(isCorrect)
'''
#logical Operator
#AND, OR, NOT, NAND, NOR, XOR, XNOR
x = 5
y = 10
z = 15

isCorrect = z > y and y > x #TRUE #TRUE
print(isCorrect) #true
isCorrect = x > z and y > x #FALSE #true
print(isCorrect) #false

isCorrect = z > y or y < x #TRUE or #TRUE
print(isCorrect) #TRUE
isCorrect = x > z or y > x #FALSE or #true
print(isCorrect) #true

isCorrect = not (x > z and x > y) #all FALSE
print ("NAND " + str(isCorrect))

#XOR
a = 10
b = 10
isCorrect = a != b
print("XOR " + str(isCorrect))

#XOR
a = 5
b = 10
c = 15
isCorrect = (a > b) != (c > a) #FALSE, TRUE, TRUE
print("XOR " + str(isCorrect))



'''

#membership
# in, is, not in, is not
myName = "Philip Charles"
yourName = "Charles"
print(myName is yourName)
print(myName is not yourName)

print (yourName in myName)
print (yourName not in myName)
print (myName in yourName)

myFavortieFruits = ["apple", "banana", "mango"]
print("apple" in myFavortieFruits)
print("orange" in myFavortieFruits)