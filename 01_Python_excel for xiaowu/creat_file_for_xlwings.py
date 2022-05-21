"""
Created by hu-jinwen on 2022/5/3
"""
# 导入xlwings模块
import xlwings as xw

# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄，屏幕更新关闭
app = xw.App(visible=True, add_book=False)
app.display_alerts = False
app.screen_updating = False

# 文件位置：filepath，打开test文档，然后保存，关闭，结束程序
# personal_inf = r'./python_learn/01_Python_excel_for_xiaowu'
# wb = app.books.open(personal_inf)
# wb.save()
# wb.close()
# app.quit()

wb = app.books.add()
# wb.save(r'd:\test.xlsx')

# wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值
# wb.sheets['sheet1'].range('A1').value = '人生'
wb.save('help')
wb.close()
app.quit()