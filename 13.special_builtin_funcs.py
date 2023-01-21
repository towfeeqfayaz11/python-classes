#lst1 = ["2", "4", "6", "8"]
from functools import reduce

# map ----------------------------------------

# res1 = list( map(int , lst1) )
# print(lst)
# print(res)

# def toSqr(arg):
#     return arg*arg

lst2 = [1,2,3,4,5,6,7,8]

res2 = list(map(lambda x:x*2, {1,2,3,4}))
# # print(lst2)
#print(res2)


# filter ----------------------------------------
oddNumsArr = list(filter(lambda x:x>2, {1,2,3,4}))
# print(oddNumsArr)

# reduce ----------------------------------------
arrSum = reduce(lambda x,y: x+y, lst2)
print(arrSum)