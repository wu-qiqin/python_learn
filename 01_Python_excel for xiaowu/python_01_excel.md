## Excel 中新建一个工作簿，然后往里添加sheet(新建工作簿&增加sheet)
```python
#一个excel表格中可以添加多个sheet
1. f = xlwt.Workbook()  # 创建工作簿
2. sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
```

## 往sheet中写入内容: sheet.write函数可以传三个参数
```python
第i（参数1）第j（参数2）列存入内容（参数3）

1. sheet1.write(i, j, '第i行第j列存放此内容', style)
2. # 这条语句实现的功能就是往第i行第j列存第三个参数的内容，
3. #第四个参数是样式(如字体，背景)，可以不传第四个参数。
```


## 合并单元格并写入内容：
```python
1. sheet1.write_merge(x, x + m, y, y + n, '内容', style)
2. # 这条y语句表示将[x:x+m]行[y:y+n]列的矩阵合并成一个单元格。存放第五个参数的#内容，同理，style参数可以不传参

```
## 最后使用f.save(‘demo’)



## Excel 中日期处理：

```python


判断ctype是否等于3，如果等于3，则用时间格式处理：

if (sheet.cell(row,col).ctype == 3):
    date_value = xlrd.xldate_as_tuple(sheet.cell_value(rows,3),book.datemode)
    date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')



```

## Excel 中获取合并单元格的值：
```python

for (rlow, rhigh, clow, chigh ) in sheet.merged_cells:
    merge.append([rlow,clow])
    print(merge)

for index in merge:

    print(sheet.cell_value(index[0], index[1]))

```

## Excel 中获取** 行/列 内容
```python

01: 打开文件：
for i in range(len(workbook.sheet_names())):
    # 打开第一个列表
    # 打开第二个列表
    sheet0 = workbook.sheet_by_index(0)
    sheet1 = workbook.sheet_by_name(u'xiaowu')

02： 获取行列信息：
print(sheet0.row_values(1))
print(sheet0.col_values(2))

```

## Excel中获取单元格内容+ 数据类型
```python

# 01 获取单元格内容
print (sheet0.cell(1,0).value)

# 02 获取单元格内容的数据类型
print (sheet0.cell_type(1,1))
print(sheet.0(1,1).ctype)
#ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
```

## 安装插件
```python

01:
pip install ***

02:

easy_install ***

```

## xlutils中copy功能
```python
import xlrd
from xlutils.copy import copy
f = xlrd.open_workbook(r'xlwt_tutorial')
wb = copy(f) # 将f拷贝到wb
sheet1 = wb.get_sheet(0) # 打开sheet
print (sheet1.name)
sheet1.write(3,0,'change')
wb.save('xlwt_tutorial')


```