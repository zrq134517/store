m=0
a=int(input())
b=int(input())
c=int(input())
if     a>b:
       m=a
       a=b
       b=m
if   b>c:
       n = b
       b = c
       c = n
if     a>b:
       m=a
       a=b
       b=m
print(a,b,c)
if a+b>c:
   print("能形成三角形")
   if a==b==c:
       print("等边三角形")
   elif a == b :
       print("等腰三角形")
   elif a*a+b*b==c*c:
        print("直角三角形")
   else:
       print("普通三角形")
else:
   print("不能形成三角形")



