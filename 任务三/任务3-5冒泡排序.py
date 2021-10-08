a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
temp=0
for j in range(len(a)-1):
    for i in range(len(a)-j-1):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
print(a)