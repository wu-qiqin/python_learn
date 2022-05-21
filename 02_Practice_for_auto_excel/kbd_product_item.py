"""
Created by hu-jinwen on 2022/5/6
"""
import xlrd

from prcatice_xlrd import KBDProductItem

workbook = xlrd.open_workbook("器件涨价清单汽大众.xls")
sheet = workbook.sheet_by_index(2)
rows = sheet.get_rows()

row_list = []

for row in rows:
    col_value_01 = row[5]
    col_value_02 = row[9]
    col_value_03 = row[6]

    cite_item = KBDProductItem()
    cite_item.kbd_id = col_value_01.value
    cite_item.specification = col_value_02.value
    cite_item.customer_id = col_value_03.value

    row_list.append(cite_item)

print(row_list)