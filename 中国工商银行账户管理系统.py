import random
bank_name="汉科软地球中国区老牛湾分行"#全局变量
bank={}
#功能1、添加用户
##1：成功，2：用户已存在，3：用户库已满
def useradd():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")#print(bank[username]["password"])
    print("下面请您输入你的地址")
    country=input("\t\t请输入你所在的国家：")
    province=input("\t\t请输入您的省份：")
    street=input("\t\t请输入你的街道：")
    door=input("\t\t请输入您的门牌号：")
    account=random.randint(10000000,99999999)
    status=bank_useradd(username,password,country,province,street,door,account)
         #             元素1    元素2    元素3
    if status == 1:
        print("恭喜您成功开户，以下是您的个人信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
    if status == 2:
            print("用户账号已存在，请重新开户！")
    if status == 3:
            print("恭喜您成功开户，以下是您的个人信息：")
            info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                密码：*****
                                国籍：%s
                                省份：%s
                                街道：%s
                                门牌号：%s
                                余额：%s
                                开户行名称：%s
                            '''
            # 每个元素都可传入%
            print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
            print("用户库已注册满!")
    #开户信息
def bank_useradd(username,password,country,province,street,door,account):
        if account in bank:
            return 2
        else:
            bank[account]={
             "用户名": username,
             "账号":    account,
             "密码":password,
             "国籍":country,
             "省份":province,
             "街道":street,
             "门牌号":door,
             "开户行名称":bank_name,
             "money":0}
            if len(bank) ==100:
                return 3
            return 1
#功能2存钱
def cq():
    n = 1
    while n == 1:
        zh = int(input("请输入您的账号："))
        if zh in bank:
            m = int(input("请输入存入的金额："))
            bank[zh]["money"]=bank[zh]["money"]+m
            print("存入成功！")
            print("账户",bank[zh]["账号"],"现有金额为：", bank[zh]["money"],"元")
            break
        else:
            n=False
            print("**该用户不存在**")
#功能3取钱
def qq():
    n = 0
    while n == 0:
        zh = int(input("请输入您的账号："))
        if zh in bank:
            m = input("请输入您的密码：")
            if m in bank[zh]["密码"]:
                print("余额：", bank[zh]["money"])
                j= int(input("请输入要转出的金额："))
                if j<=bank[zh]["money"]:
                    bank[zh]["money"]=bank[zh]["money"]-j
                    print("转出成功！")
                    break
                else:
                    print("**余额不足**")
                    return 3
            else:
                 print("**密码错误**")
                 return 1
        else:
            print("**该用户不存在**")
            return 2

#功能4转账
def zz():
    n = 0
    while n == 0:
        c = int(input("请输入转出的账号："))
        if c in bank:
            r = int(input("请输入转入的账号："))
            if r in bank and r!=c:
                m = input("请输入转出账号的密码：")
                if m in bank[c]["密码"]:
                   print("余额：", bank[c]["money"])
                   j = int(input("请输入要转出的金额："))
                   if j <= bank[c]["money"]:
                       bank[c]["money"] = bank[c]["money"] - j
                       bank[r]["money"] = bank[r]["money"] + j
                       print("转账成功！")
                       break
                   else:
                       print("**余额不足**")
                       return 3
                else:
                    print("**密码错误**")
                    return 2
            else:
                print("**该用户不存在**")
                return 1
        else:
            print("**该用户不存在**")
            return 1

#功能5查询
def  chaxun():
    n=1
    while n==1:
          zh = int(input("请输入您的账号："))
          if zh in bank:
             m = input("请输入您的密码：")
             if m in bank[zh]["密码"]:
                print("------------用户",bank[zh]["用户名"],"的个人信息 - -----------")
                print("   用户名：", bank[zh]["用户名"])
                print("   当前账号：", bank[zh]["账号"])
                print("   密码：", bank[zh]["密码"])
                print("   余额：", bank[zh]["money"])
                print("   用户居住地址：", bank[zh]["国籍"], bank[zh]["省份"], bank[zh]["街道"], bank[zh]["门牌号"])
                print("   当前账户的开户行：", bank[zh]["开户行名称"])
             else:print("**密码错误**")
          else:print("**该用户不存在**")
          q = int(input("继续查询-1   退出查询业务-0"))
          if q==0:
              n=0
#6、退出
def  bye():
    print("**********************************************")
    print("*                 系统已退出                   *")
    print("*                欢迎下次使用                  *")
    print("**********************************************")
#***************选择业务***********************
while True:
    print("**********************************************")
    print("*           中国工商银行账户管理系统              *")
    print("**********************************************")
    print("*            1、开户                          *")
    print("*            2、存钱                          *")
    print("*            3、取钱                          *")
    print("*            4、转账                          *")
    print("*            5、查询                          *")
    print("*            6、Bye!                         *")
    print("**********************************************")
    begin = input("请选择业务：")
    if begin == "1":   #开户
         useradd()
         print("已存在账户：")
         print(bank)
    elif begin == "2":  #存钱
         cq()
    elif begin == "3":  #取钱
         qq()
    elif begin == "4":   #转账
         zz()
    elif begin == "5":   #查询
         chaxun()
    elif begin == "6":   #退出系统
         bye()
         break
    else:
         print("输入错误，请重新输入！")
