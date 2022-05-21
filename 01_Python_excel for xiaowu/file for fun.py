"""
Created by hu-jinwen on 2022/5/5
"""
import xlrd

data = xlrd.open_workbook('personal inf.xls')
sheet_name = data.sheet_names()
print(sheet_name)

data1 =  xlrd.open_workbook('test_excel.xls')
sheet_name1 = data1.sheet_names()
print(sheet_name1)
sheet_name2 = data1.sheet_names()[1]
sheet3 = data1.sheet_by_index(0)
print(sheet_name2)
print(sheet3)
print('sheet3名称:{}\nsheet3列数: {}\nsheet3行数: {}'.format(sheet3.name, sheet3.ncols,sheet3.nrows))
print(sheet3.cell_value(1,1))
print(sheet3.cell_type(1,1))
print(sheet3.cell(1,1).ctype)

# from datetime import datetime, date
#
# if sheet3.cell(1, 1).ctype == 3:
#     print(sheet3.cell(1, 1).value)  # 41463.0
#     date_value = xlrd.xldate_as_tuple(sheet3.cell(1, 1).value, data.datemode)
#     print(date_value)  # (2013, 7, 8, 0, 0, 0)
#     print(date(*date_value[:3]))  # 2013-07-08
#     print(date(*date_value[:3]).strftime('%Y/%m/%d'))  # 2013/07/08
#
# from datetime import datetime, date
# if sheet3.cell(1,1).ctype == 3:
#     print(sheet3.cell(1,1).va
#     date_value = xlrd.xldate_as_tuple(sheet3.cell(1,1).value, date.)
#     print(date_value)
#     print(date(*date_value[:3]))


import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("help", cell_overwrite_ok=True)
ws.write(0,1, "00000")
wb.save("help.xls")

from xlutils.copy import copy

oldwb = xlrd.open_workbook("help.xls")
newwb = copy(oldwb)
newws = newwb.get_sheet(0)
newws.write(2, 3, "10000")
newwb.save("help.xls")


