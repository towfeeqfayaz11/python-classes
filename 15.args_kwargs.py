#tuple packing
# a = (1,2,3,4,5)

# # tuple unpacking
# b,c,d,e,f = a

# print(b)

#####################################

# * before a variable makes it a special variable which can store the multiple passed elements as tuple
# when using the *args variable, use it without a *
# def addNums(*args):
#     print(args)
    
#     x,*a = args
#     print(type(a))

#     print(x,a)

# addNums(1,2,3)
# addNums(1,2,3,4,5,6)


######################################
# def fun(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(type(kwargs))

# fun(1,2,3, a=[1,2,3],b=20,c=30)



# def fun1(a,*args,b=10, **kwargs):
#     print(a,b)
#     print(args, kwargs)

# fun1(1,2,3,4,5,x=11,y=12)


# def fun2(a,b=1,*args, **kwargs):
#     print(a,b)
#     print(args)
#     print(kwargs)

# fun2(11,12,13,14,15,x=1, y=2,z=3)

######################################


# x,y -> required arguments
# z   -> default argument
# *args, **kwargs -> optional arguments
# def fun1(x, y, z=0, *args, **kwargs):
#     print(x)
#     print(y)
#     print(z)
#     print(args)
#     print(kwargs)

# fun1(1,2,3,4,5,6,7)