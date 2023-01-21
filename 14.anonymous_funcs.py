# anonymous functions -> a function which doesn't have a name



def addNums(x,y):
    return x+y

print(addNums(3,4))



print((lambda x,y:x+y)(3,4))

addfun = (lambda x,y:x+y)
print(addfun(5,6))
