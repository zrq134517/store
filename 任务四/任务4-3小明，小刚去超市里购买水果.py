'''
小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，
请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
以姓名做key，value仍然是字典
'''       # 水果和单价
Friuts = {'苹果':12.3,'草莓':4.5,'香蕉':6.3,'葡萄':5.8,'橘子':6.4,'樱桃':15.8 }
info = {
        '小明': {
                 'fruits': {'苹果':4,'草莓':13,'香蕉':10},
                 'money':0 },
        '小刚': {
                 'fruits': {'葡萄':19,'橘子':12,'樱桃':30},
                 'money': 0}
        }
n=0
m=0
x=0
while x<2:
    mycart={}
    a=input("请输入姓名：")      #     地球         \
    if a in info.keys():
          mycart =info[a]['fruits']
          print(a,"的fruits为",mycart)
    for i in mycart:
        for j in Friuts:
            if i==j:
                n=mycart[i]*Friuts[j]
                m=m+n
    print(a,"的花费的金额为",m)
    info[a]['money']=m
    x=x+1
    if x==2:
       print(info)