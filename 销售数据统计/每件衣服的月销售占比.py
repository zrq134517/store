import xlrd
wb = xlrd.open_workbook(filename=r"C:\Users\Administrator\PycharmProjects\excel表\2020年每个月的销售情况.xlsx",
                       encoding_override=True)
l = []
for i in range(0,12):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows # 获取多少行
        cols = sheet.ncols # 获取多少列
        sum1 = 0
        xlsum = 0
        for j in range(1, rows):
            data = sheet.row_values(j)
            sum1 = sum1 +data[4]
            if data[1] in l:
                continue
            else:l.append(data[1])
        xlsum = xlsum + sum1
        n = 0
        for k in range(0, len(l)):
            n = 0
            for j in range(1, rows):
                data = sheet.row_values(j)
                if data[1] == l[k]:
                    n = n + data[4]
            print(l[k], i+1,"月月销售占比", n/xlsum*100,"%")
        print()