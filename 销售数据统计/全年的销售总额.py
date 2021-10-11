import xlrd
wb = xlrd.open_workbook(filename=r"C:\Users\Administrator\PycharmProjects\excel表\2020年每个月的销售情况.xlsx",
                        encoding_override=True)
# 全年的销售总额
qnsum = 0
for i in range(0, 12):
    sheet = wb.sheet_by_index(i)
    rows = sheet.nrows  # 获取多少行
    cols = sheet.ncols  # 获取多少列
    sum0 = 0
    for j in range(1, rows):
        data = sheet.row_values(j)
        sum0 = sum0 + data[2] * data[4]
    qnsum = qnsum + sum0
print("1.全年的销售总额销售总额：￥", qnsum)