import xlrd
wb = xlrd.open_workbook(filename=r"C:\Users\Administrator\PycharmProjects\excel表\2020年每个月的销售情况.xlsx",
                        encoding_override=True)
xlsum = 0
l = []
qnsum=0
for i in range(0, 12):
    sheet = wb.sheet_by_index(i)
    rows = sheet.nrows  # 获取多少行
    cols = sheet.ncols  # 获取多少列
    sum1 = 0
    sum2 = 0
    sum0 = 0
    for j in range(1, rows):
        data = sheet.row_values(j)
        sum0 = sum0 + data[2] * data[4]
    qnsum = qnsum + sum0
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
    for i in range(0, 12):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows  # 获取多少行
        cols = sheet.ncols  # 获取多少列
        for j in range(1, rows):
            data = sheet.row_values(j)
            if data[1] == l[k]:
                n = n + data[4]
                m = m + data[4] * data[2]
    print(l[k],"销售（件数）占比",n/xlsum*100,"%", "   ,销售额占比", m / qnsum * 100, "%")