def outer(func):
    def inner(n):
        print(n, end=" ")
        func()
    return inner


@outer
def greet():
    print("Hello")

name = "vijay"


greet(name)


# when line 16 executes; below steps happen
#   1) outer function is getting called
#   2) when outer is getting called, it creates a definition of a funciton called inner
#   3) it returns the reference to inner func
#   4) it calls the inner func