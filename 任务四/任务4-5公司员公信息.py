#
l=        ["姓名","年龄","性别","编号","任职公司","薪资","部门编号"]
names = [  ["刘备","56", "男", "106", "IBM",    500,   "50"],
           ["大乔","19", "女", "230", "微软",    501,   "60"],
           ["小乔","19", "女", "210", "Oracle", 600,   "60"],
           ["张飞","45", "男", "230", "Tencent",700,   "10"]
        ]
#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
m=[]
n=[]
name={}
w={}
x=0
for i in range(len(names)):
    m.append(names[i][0])
    for j in range(len(names)+2):
        n.append(names[i][j + 1])
    s = []
    for j in range(x, x + len(names) + 2):
        s.append(n[j])

for i in range(len(names)):
    x=x+len(names)+2
    for i in range(len(s)):
        w[l[i+1]] = s[i]
    for i in range(len(names)):
        name[m[i]] = w
print(name)
