#List = [1,2,3,4,5,6,7,8,9]
#实现效果：list = [9,8,7,6,5,4,3,2,1]
list=[1,5,21,30,15,9,30,24]
a=0
print("原数列：")
for i  in range(len(list)):
    print(list[i])
print("共有",i+1,"个数")
print("实现数列：")
for i  in range(1,i+2):
    print(list[a-i])