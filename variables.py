# types of data in python

# int     -   5, 6 , 7
# float   -  4.569076,  89.220          
# string  - "Hello World", 'jack'
# bool    - True , False       false
# complex - 3 + 4j
#               2j
           

# NOTE : python by default doesn't support implicit type conversion
# type converison means converting one type of data to other

a = 5
b = 4.55



print("hello", a, b)
print(type(a), type(b))

c = "Hello" + str(a)
#5    -->  str(a)     --> "5"

print(c, type(c))


cp = 4j
print(cp, type(cp))