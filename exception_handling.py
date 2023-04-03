# try:
#     # the code that might give exception, should always go tot try block
#     pass
# except:   # except will only execute if there is exception
#     pass
# else:     # else will only execute if there is no exception
#     pass
# finally:  # will excute for both exception and no exception cases
#     pass



try:
    a = 11
    b = 0
    ans = a/b
    print(ans)
except AttributeError:
    print("atribute error occured")
except ZeroDivisionError:
    print("cant divide by zero")
except Exception as e:
    print("their is an exception", e)
else:
    print("there is no exception")
finally:
    print("finally always")



# a = 11
# b = 0
# ans = a/b
# print(ans)