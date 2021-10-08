import random
from yhsjk import select
from yhsjk import update
bank_name="汉科软地球中国区老牛湾分行"#全局变量
money=0
info = '''                    ------------个人信息------------
                    用户名:%s
                    账号：%s 密码：*****
                    国籍：%s 省份：%s 街道：%s 门牌号：%s
                    余额：%s
                    开户行名称：%s'''
#功能1、添加用户
##1：成功，2：用户已存在，3：用户库已满
def useradd():
    username=input("请输入您的用户名：")
    password=input("请输入您的密码：")#print(bank[username]["password"])
    print("下面请您输入你所在的地址")
    country=input("\t\t请输入您所在的国家：")
    province=input("\t\t请输入您所在的省份：")
    street=input("\t\t请输入您所在的街道：")
    door=input("\t\t请输入您所在的门牌号：")
    account=random.randint(10000000,99999999)
    status=bank_useradd(username,password,country,province,street,door,account)
    if status == 1:
        print("恭喜您成功开户，以下是您的个人信息：")
        print(info % (username, account, country, province, street, door, money, bank_name))
        print("请牢记账号，切勿遗忘！！！")
    elif status == 2:print("该用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")
    #开户信息
def bank_useradd(username,password,country,province,street,door,account):
    # 查询是否已满
    sql1 = "select count(*) from user"
    param1 = []
    data = select(sql1, param1)  # ((100),)
    if data[0][0] >= 100:return 3
    # 查询是否存在
    sql2 = "select * from user where username  = %s"
    param2 = [username]
    data2 = select(sql2, param2)
    if len(data2) != 0:return 2
    # 插入数据
    sql3 = "insert into user  values(%s,%s, %s, %s,%s,%s,%s,%s,%s)"
    param3 = [ account,username,password,country,province,street,door,0,bank_name]
    update(sql3, param3)
    return 1
#功能2存钱
def cq():
        account = input("请输入您的账号：")
        m = int(input("请输入存入的金额："))
        n=cq_1(account)
        if n==1:
            if m>=0:
               sql2 = "update user set money  = money+%s where account = %s"
               param2 = [m,account]
               update(sql2, param2)
               print("恭喜您存钱成功")
               sql3 = "select * from user where account  = %s"
               param3 = [account]
               data3 = select(sql3, param3)
               print("------------个人信息------------")
               print("  用户名:", data3[0][1])
               print("  账号:", data3[0][0], "密码:", data3[0][2])
               print("  国籍:", data3[0][3], "省份:", data3[0][4], "街道:", data3[0][5], "门牌号:", data3[0][6])
               print("  余额:", data3[0][7])
               print("  开户行名称:", data3[0][8])
            else:print("对不起，您输入的金额非法！！！")
        else:print("对不起，您的个人信息不存在！请先开户后再次操作！")
def cq_1(username):
    sql1 = "select * from user where account  = %s"
    param1 = [username]
    data1 = select(sql1, param1)
    if len(data1) != 0:return 1
    else:return False
#功能3取钱
def qq():
        zh = int(input("请输入您的账号："))
        m = input("请输入您的密码：")
        j = int(input("请输入要取出的金额："))
        n=qq_1(zh, m, j)
        if   n==1:print("对不起，该账户个人信息不存在！")
        elif n==2:print("**取钱失败！密码错误**")
        elif n==3:print("**取钱失败！该用户余额不足**")
        else:
            print("恭喜您取钱成功")
            sql3 = "select * from user where account  = %s"
            param3 = [zh]
            data3 = select(sql3, param3)
            print("------------个人信息------------")
            print("  用户名:", data3[0][1])
            print("  账号:", data3[0][0], "密码:", data3[0][2])
            print("  国籍:", data3[0][3], "省份:", data3[0][4], "街道:", data3[0][5], "门牌号:", data3[0][6])
            print("  余额:", data3[0][7])
            print("  开户行名称:", data3[0][8])
def qq_1(zh,m,j):
    sql1 = "select * from user where account  = %s"
    param1 = [zh]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        sql2 = "select * from user where account  = %s and password  = %s"
        param2 = [zh, m]
        data2 = select(sql2, param2)
        if j < 0:print("对不起，您输入的金额非法！！！")
        else:
           if len(data2) != 0:
               sql3 = "SELECT money FROM  user WHERE account  = %s"
               param3 = [zh]
               data3 = select(sql3, param3)
               if data3[0][0]>=j:
                  sql4 = "update user set money  = money-%s where account = %s "
                  param4 = [j, zh]
                  update(sql4, param4)
                  return 0
               else:return 3
           else:return 2
    else:return 1
#功能4转账
def zz():
        c = int(input("请输入转出账号："))
        r = int(input("请输入转入账号："))
        m = input("请输入转出账号密码：")
        j = int(input("请输入要转出金额："))
        n=zz_1(c,r,m,j)
        if   n==1:print("**转出或转入账号不存在**")
        elif n == 2:print("**转出账号密码错误**")
        elif n == 3:print("**转出账号余额不足**")
        elif n == 0:print("转账成功！")
def zz_1(c,r,m,j):
    sql1 = "select * from user where account  = %s"
    param1 = [c]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        sql2 = "select * from user where account  = %s "
        param2 = [r]
        data2 = select(sql2, param2)
        if len(data2) != 0:
            sql3 = "select * from user where account  = %s and password  = %s"
            param3 = [c,m]
            data3 = select(sql3, param3)
            if j < 0:print("对不起，您输入的金额非法！！！")
            else:
                if len(data3) != 0:
                    sql4 = "SELECT money FROM  user WHERE account  = %s"
                    param4 = [c]
                    data4 = select(sql4, param4)
                    if data4[0][0] >= j:
                        sql5 = "update user set money  = money-%s where account = %s "
                        param5 = [j, c]
                        update(sql5, param5)
                        sql6 = "update user set money  = money+%s where account = %s "
                        param6 = [j, r]
                        update(sql6, param6)
                        sql7 = "select * from user where account  = %s "
                        param7 = [c]
                        data7 = select(sql7, param7)
                        print("------------个人信息------------")
                        print("  用户名:", data7[0][1])
                        print("  账号:", data7[0][0], "密码:", data7[0][2])
                        print("  国籍:", data7[0][3], "省份:", data7[0][4], "街道:", data7[0][5], "门牌号:", data7[0][6])
                        print("  余额:", data7[0][7])
                        print("  开户行名称:", data7[0][8])
                        return 0
                    else:return 3
                else:return 2
        else:return 1
    else:return 1
#功能5查询
def chaxun():
    zh = input("请输入您的账号：")
    m = input("请输入您的密码：")
    chaxun_1(zh, m)
def chaxun_1(zh,m):
    sql1 = "select * from user where account  = %s"
    param1 = [zh]
    data1 = select(sql1, param1)
    if len(data1) != 0:
        sql2 = "select * from user where account  = %s and password  = %s"
        param2 = [zh,m]
        data2 = select(sql2, param2)
        if len(data2) != 0:
           print("------------个人信息------------")
           print("  用户名:", data2[0][1])
           print("  账号:", data2[0][0], "密码:", data2[0][2])
           print("  国籍:", data2[0][3], "省份:", data2[0][4], "街道:", data2[0][5], "门牌号:", data2[0][6])
           print("  余额:", data2[0][7])
           print("  开户行名称:", data2[0][8])
        else:print("**密码错误**")
    else:print("**该用户不存在**")
#功能6退出系统
def bye():
    print("**********************************************")
    print("*                 系统已退出                   *")
    print("*                欢迎下次使用                  *")
    print("**********************************************")
#***************主菜单 ：选择业务***********************
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
    if   begin == "1":useradd()#开户
    elif begin == "2":cq()#存钱
    elif begin == "3":qq()#取钱
    elif begin == "4":zz()#转账
    elif begin == "5":chaxun()#查询
    elif begin == "6":
         bye()#退出系统
         break
    else:print("输入错误，请重新输入！")


