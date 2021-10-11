import xlrd
wb = xlrd.open_workbook(filename=r"C:\Users\Administrator\PycharmProjects\excel表\2020年每个月的销售情况.xlsx",
                        encoding_override=True)
y=[[2,3,4],[5,6,7],[8,9,10],[11,0,1]]
jd=0
for x in range(0,4):
    jd=jd+1
    xlsum = 0
    l = []
    d = []
    ll = []
    for i in y[x]:
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows  # 获取多少行
        cols = sheet.ncols  # 获取多少列
        sum1 = 0
        sum2 = 0
        for j in range(1, rows):
            data = sheet.row_values(j)
            sum1 = sum1 + data[4]
            if data[1] in l:
                continue
            else:
                l.append(data[1])
        xlsum = xlsum + sum1
    for k in range(0, len(l)):
        n = 0
        m = 0
        for i in y[x]:
            sheet = wb.sheet_by_index(i)
            rows = sheet.nrows  # 获取多少行
            cols = sheet.ncols  # 获取多少列
            for j in range(1, rows):
                data = sheet.row_values(j)
                if data[1] == l[k]:
                    n = n + data[4]
                    m = m + data[4] * data[2]
        ll.append(n)
        d.append((l[k],n))
    temp=0
    for j in range(len(ll)-1):
        for i in range(len(ll)-j-1):
            if ll[i]>ll[i+1]:
                temp=ll[i]
                ll[i]=ll[i+1]
                ll[i+1]=temp
    for i in range(0, len(d)):
        if d[i][1]==ll[0]:
           print("第",jd,"季度最畅销的衣服是",d[i][0])


