'''
3、写一个判断是否为三角形的函数
parseTrigon(a,b,c)。(语 言请优先使用
python> java>C>其它)
入参: a,b,c三个字符串代表三边，要求在
函数内部判断各边长均为1~ 10的整数。
返回值:有4种可能: -1(边长不合法)，0(
非三角形、即存在两边之和不大于第三边)
1(普通三角形), 2(等边三角形), 3(等边
三角形);
'''
m=0
def sj(a,b,c):
    if 0<a<=10 and 0<b<=10 and 0<b<=10:
        if  a>b:
            m=a
            a=b
            b=m
        if  b>c:
            n = b
            b = c
            c = n
        if  a>b:
            m=a
            a=b
            b=m
        if a+b>c:
           if a==b==c:return 4
           elif a == b :return 3
           elif a*a+b*b==c*c:return 2
           else:return 1
        else:return 0
    else:return -1
while True:
   a=int(input())
   b=int(input())
   c=int(input())
   n=sj(a,b,c)
   if n==-1:print("边长不合法")
   if n==0:print("非三角形")
   if n == 1: print("普通三角形")
   if n == 2:print("直角三角形")
   if n == 3:print("等腰三角形")
   if n == 4:print("等边三角形")