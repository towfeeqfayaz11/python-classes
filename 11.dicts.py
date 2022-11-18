# dict
# key can be only immutable
# value can be mutable or immutable
# dict is mutable

d1 = {
    "k1": "v1", 
    "k2":"v2", 
    "k3":"v3",
    "k4": "v3"
    }

for i in d1:
    print(i, d1[i])



print(d1["k1"])