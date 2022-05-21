"""
Created by hu-jinwen on 2022/5/3
"""

import xlwt


workbook = xlwt.Workbook()  # 创建工作簿

sheet0 = workbook.add_sheet('scores recording', cell_overwrite_ok=True)

mdict = {"monkey": {"writing": 80, "reading": 60, "speaking": 70, "listening": 60},
         "grape": {"writing": 100, "reading": 80, "speaking": 70, "listening": 60}}

sheet0.write(0, 0, u'scores')
sheet0.write(1, 0, u'calligraphy')
sheet0.write(2, 0, u'reading')
sheet0.write(3, 0, u'speaking')
sheet0.write(4, 0, u'listening')

temp = ['writing', 'reading', 'speaking', 'listening']

for i, item in enumerate(mdict):

    for j, val in enumerate(item):

        sheet0.write(i, j, val)


workbook.save('得分统计.xls')
