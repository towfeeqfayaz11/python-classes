def addArrays(arr1, arr2):
    resArr =[]
    for i in range(len(arr1)):
        resArr.append(arr1[i] + arr2[i])
    return resArr


# assume length is same for both the arrays
arr1 = [1,2,3,4,5,6,7]
arr2 = [0,6,7,4,2,5,1]
#       0 1 2 3 4 5 6
res =  addArrays(arr1, arr2)
print(res)

# res = [1,8,10,8,7,11,8]

arr3 = [1,2,3,4,5,9,8]

res2 = addArrays(arr3, res)
print(res2)


