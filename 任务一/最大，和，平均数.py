n=0
m=0
max=0
while m<10:
     num=int(input())
     if num>max:
        max=num
     m=m+1
     n=n+num
print("和=",n)
print("平均数=",n/10)
print("最大数=",max)