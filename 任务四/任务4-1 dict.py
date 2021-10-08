dict = {"k1":"v1",
        "k2":"v2",
        "k3":"v3"}

#1、请循环遍历出所有的key
for i in dict:
    print(i,end="")
print()
#2、请循环遍历出所有的value
for i in dict:
    print(dict[i],end="")
print()
# 3、请在字典中增加一个键值对,"k4":"v4"
dict["k4"] ="v4"
print(dict)


