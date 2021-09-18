#求其中是5的倍数的和
n=0
list=[1,5,21,30,15,9,30,24]
for i  in range(len(list)):
    if list[i]%5==0:
       n=n+list[i]
print("5的倍数的和：",n)