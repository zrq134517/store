names = [
    # 姓名  年龄  性别  编号 任职公司    薪资 部门编号
    ["曹操","56","男","106","IBM",    500 ,"50"],
    ["大乔","19","女","230","微软",    501 ,"60"],
    ["小乔","19","女","210","Oracle", 600, "60"],
    ["许褚","45","男","230","Tencent",700 ,"10"]
]
#1.统计每个人的平均薪资
m=0
s=0
i=0
for i in range(len(names)):
    m=m+names[i][5]
print("平均薪资=",m/len(names))
#2.统计每个人的平均年龄
for i in range(len(names)):
    s=s+int(names[i][1])
print("平均年龄=",s/len(names))

#3.公司新来一个员工，刘备，45，男，220，alibaba，500,30，添加到列表中
l=["刘备","45","男","220","libaba",500,"30"]
names.append(l)
print("加入新员工后：")
print(names)
#4.统计公司男女人数
a=0
b=0
for i in range(len(names)):
    if names[i][2]=="男":
        a=a+1
    else:b=b+1
print("男:",a,"女:",b)
#5.每个部门的人数
bm=[]
nm=[]
for i in range(len(names)):
    if names[i][6] in bm:
       continue
    else:bm.append(names[i][6])
for i in range(len(names)):
       nm.append(names[i][6])
for b in bm:
    j=0
    for c in nm:
        if c==b:j=j+1
    print("部门为",b,"的共",j,"人")