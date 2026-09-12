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