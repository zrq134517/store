#（1）添加登陆功能，登陆后才能进行购物操作。
#（2）添加结算积分添加功能。
#（3）登陆成功后系统随机分发一张优惠券（免单券6张，免半券3张，满600减100券50张，满10000减1000券10张，无券）前提是优惠券存在列表中。
import random
print("欢迎光临商城")
# 1.商品
shop = [
    #角标   0        ,     1
    ["机械革命       ",15000],  #0 print(shop[0][1])=15000
    ["HUAWEI watch  ",1200], #1 print(shop[1][1])=1200
    ["MAC PC        ",13000 ], #2 print(shop[2][1])=13000
    ["Iphone 54 plus",45000], #3 print(shop[3][1])=45000
    ["辣条           ",2.5], #4 print(shop[4][1])=2.5
    ["老干妈         ",13]  #5 print(shop[5][1])=13
]
#print(shop[0][0])
#2.初始化你的金额
moeny=int(input("请输入你的金额："))#str
n=moeny
#3.准备一个空的购物车
mycart=[]
#优惠券  免单券6张，免半券3张，满600减100券50张，满10000减1000券10张，无券
ran=random.randint(1,70)
if   1<=ran<=6:
     print("恭喜抽中一张免单券^_^")
elif 7<=ran<=9:
     print("恭喜抽中一张免半券^_^")
elif 10<=ran<=59:
     print("恭喜抽中一张满600减100券^_^")
elif 60<=ran<=69:
     print("恭喜抽中一张满10000减1000券^_^")
else:print("感谢参与，您没有抽中任何奖券")
#4.购买
i=1
while True: #永远循环
    shop = [
        # 角标   0        ,     1
        ["机械革命       ", 15000],  # 0 print(shop[0][1])=15000
        ["HUAWEI watch  ", 1200],  # 1 print(shop[1][1])=1200
        ["MAC PC        ", 13000],  # 2 print(shop[2][1])=13000
        ["Iphone 54 plus", 45000],  # 3 print(shop[3][1])=45000
        ["辣条           ", 2.5],  # 4 print(shop[4][1])=2.5
        ["老干妈         ", 13]  # 5 print(shop[5][1])=13
    ]
    print("商品号   商品名             价格")
    for index,value in enumerate(shop):#枚举，把角标和角标对应的内容进行整体打印
        print(" ",index," ",value)#打印所有的商品
    print("输入Q或q退出商城")
    chose=input("请输入你想要的商品号：")#int 如果你一开始就是数字，那么下面的if就没有意义
    if chose.isdigit():#isdigit-判断是否为数字
        chose =int(chose)
        if chose>len(shop)-1:#你输入的角标，如果大于商品的长度就执行代码
            print()
            print("你所输入的商品不存在,请重新输入！","余额还剩:",moeny)
            continue
        if moeny>= shop[chose][1] :#你原有存款和商品价格对比
            mycart.append(shop[chose])#加入购物车
            moeny=moeny-shop[chose][1]#存款减去商品价格
            print()
            print("恭喜你购买成功，已经加入购物车！余额还剩:",moeny,"元")
            if moeny==0:
               print("余额已用尽，购物结束！")
               print("欢迎下次光临，下面的是您的小票:")
               print("购物序列号  商品名            价格")
               for index, value in enumerate(mycart):
                   print("  ", index, " ", value)
               n = n - moeny
               print("共花费:", n, "元")
               print("您的余额还剩:", moeny, "元")
               break
        else:
         print("穷鬼，去买其他商品")
    elif chose == "q" or chose == "Q"or moeny==0:
        print()
        print("欢迎下次光临，下面的是您的小票:")
        print("购物序列号  商品名            价格")
        for index,value in enumerate(mycart):
            print("  ",index," ",value)
        n = n - moeny
        print("共花费:", n, "元")
        print("您的余额还剩:",moeny,"元")
        break
    else:
        print("输入非法")
