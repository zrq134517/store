'''
    Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10辣条优惠券（0.3），20机械革命优惠券（0.9）。
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
'''
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
#优惠券  10辣条优惠券（0.3），20机械革命优惠券（0.9）
ran=random.randint(1,3)
if ran==1:
   print("恭喜获得<辣条优惠券（0.3）>,第一次购买辣条3折优惠")
else:
    print("恭喜获得<机械革命优惠券（0.9）>，第一次购买机械革命9折优惠")
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
    chose=input("请输入你想要的商品号：")#int 如果你一开始就是数字，那么下面的if就没有意义
    if chose.isdigit():#isdigit-判断是否为数字
        chose =int(chose)
        if chose>len(shop)-1:#你输入的角标，如果大于商品的长度就执行代码
            print()
            print("你所输入的商品不存在,请重新输入！","余额还剩:",moeny)
            continue
        else:
            ##使用优惠券#
            while  i==1:
                  if  chose==4 and ran==1 :
                      shop[4][1] = shop[4][1] * 0.3
                      i = i - 1
                  elif chose==0:
                       shop[0][1] = shop[0][1] * 0.9
                       i = i - 1
            ####
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
                   print("您的余额还剩:", moeny, "元")
                   n = n - moeny
                   print("共花费:", n, "元")
                   break
            else:
                print("穷鬼，去买其他商品")
    elif chose == "q" or chose == "Q"or moeny==0:
        print()
        print("欢迎下次光临，下面的是您的小票:")
        print("购物序列号  商品名            价格")
        for index,value in enumerate(mycart):
            print("  ",index," ",value)
        print("您的余额还剩:",moeny,"元")
        n=n-moeny
        print("共花费:", n, "元")
        break
    else:
        print("输入非法")
