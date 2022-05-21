## xlutils可用于拷贝原excel或者在原excel基础上进行修改，并保存
```python
import xlrd
from xlutils.copy import copy

f = xlrd.open_workbook(r'test_excel.xls') # 打开想要复制或者修改的excel，赋值
wb = copy(f)  # 将f拷贝到wb
ws= wb.get_sheet(0)  # 打开sheet
print(ws.name)
ws.write(4, 0, '火龙果')
wb.save('test_excel.xls') # 保存工作簿

```

## 读取表格信息
```python

sheet = workbook.sheet_by_index(0)/workbook.sheet_by_name("Sheet1")
col2 = sheet.col_values(1)  # 取出第二列
cel_value = sheet.cell_value(1, 1)
print(col2)
print(cel_value)


```

## 写入表格信息
```python

write_save = new_workbook.get_sheet(0)
write_save.write(0, 0, "xlutils写入！")

```

