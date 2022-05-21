"""
Created by hu-jinwen on 2022/5/2
"""
import xlwt
import xlrd
from xlutils.copy import copy


workbook = xlwt.Workbook()
sheet0 = workbook.add_sheet(u'xiaohu', cell_overwrite_ok=True)
sheet1 = workbook.add_sheet(u'xiaowu', cell_overwrite_ok=True)


row = 0
row_list = [u'姓名', u'年龄', u'学校', u'专业']

for colum, context in enumerate(row_list):
    sheet0.write(row, colum, context)
row += 1
sheet0.write(row, 0, u'葡萄')
sheet0.write(row, 1, 18)
sheet0.write(row, 2, u'北京电影学院')
row += 1
sheet0.write(row, 0, u'椰子')
sheet0.write(row, 1, 20)
sheet0.write(row, 2, u'帝国国王科技大学')
row += 1
sheet0.write(row, 0, u'西瓜')
sheet0.write(row, 1, 22)
sheet0.write(row, 2, '上海戏剧学院')

sheet0.write_merge(1, 3, 3, 3, u'汉语言文学')
workbook.save('test_excel.xls')


# xlrd

workbook = xlrd.open_workbook(r'test_excel.xls')
name_list = workbook.sheet_names()
print(name_list)

for i in range(len(workbook.sheet_names())):
    # 打开第一个列表
    # 打开第二个列表
    sheet0 = workbook.sheet_by_index(0)
    sheet1 = workbook.sheet_by_name(u'xiaowu')

#输出sheet的名称,行数,列数

print(sheet0.name, sheet0.nrows, sheet0.ncols)
print(sheet1.name, sheet1.nrows, sheet1.ncols)


print(sheet0.row_values(1))
print(sheet0.col_values(2))

# 获取单元格内容
print(sheet0.cell_value(2, 2))
print(sheet0.cell_type(2, 2))


f = xlrd.open_workbook(r'test_excel.xls')
wb = copy(f)  # 将f拷贝到wb
sheet0 = wb.get_sheet(0)  # 打开sheet
print(sheet0.name)
sheet0.write(4, 0, '火龙果')
wb.save('test_excel.xls')

