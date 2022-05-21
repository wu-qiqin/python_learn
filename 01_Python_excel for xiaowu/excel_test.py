"""
Created by hu-jinwen on 2022/5/2
"""

# >>> workbook = xlrd.open_workbook(r'F:\demo.xlsx',formatting_info=True)
# >>> sheet2 = workbook.sheet_by_name('sheet2')
# >>> sheet2.merged_cells
# [(7, 8, 2, 5), (1, 3, 4, 5), (3, 6, 4, 5)]
import xlrd

workbook = xlrd.open_workbook("/Users/hujinwen/Downloads/test2.xls", formatting_info=True)
sheet = workbook.sheet_by_index(0)
cells = sheet.merged_cells
print()

# >> > merge = []
# >> > for (rlow, rhigh, clow, chigh) in sheet2.merged_cells:
#     merge.append([rlow, clow])
#
# >> > merge
# [[7, 2], [1, 4], [3, 4]]
# >> > for index in merge:
#     print
#     sheet2.cell_value(index[0], index[1])

merge = []
for (rlow, rhigh, clow, chigh ) in sheet.merged_cells:
    merge.append([rlow,clow])
    print(merge)
    # merge = [[2, 1], [6, 3], [10, 1]]

for index in merge:

    print(sheet.cell_value(index[0], index[1]))

