import random
n=500
for y in range(n):
 ran=random.randint(0,80)
 m=3
 print("谜底",ran)
 for y in range(n):
       print("剩余金额:",n,"剩余次数:",m)
       num=int(input("请输入一个数字（0-80)"))
       if   num>ran:
            print("猜大了!")
            n=n-100
            m=m-1
       elif   num<ran:
              print("猜小了!")
              n=n-100
              m=m-1
       elif num==ran:
            print("OK")
            n=n+10
            m=3
            ran = random.randint(0, 80)
            print("谜底",ran)
            continue
       if n <= 100:
           print("剩余金额不足100，游戏退出")
           break
       if m == 0:
           print("次数不足，游戏退出")
           break
 break
