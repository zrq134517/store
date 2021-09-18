'''
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
如果你的num>ran打印猜大了    <  猜小了
初始金额为500 每猜一次扣除100  如果资金为0 退出系统
如果三次没有猜中那就退出
！！！如果猜的正确的那么增加10，随机数不能只随机一次
    '''
import random
n=500
while True:
 ran=random.randint(0,80)
 m=3
 print("谜底",ran)
 while True:
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
           print("金额不足，游戏退出")
           break
       if m == 0:
           print("次数不足，游戏退出")
           break
 break








