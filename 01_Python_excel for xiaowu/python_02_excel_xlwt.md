## xlwt 

```python

class XFStyle(object):

    def __init__(self):
        
        self.num_format_str = 'Genaral'
        self.font
        self.alignment
        self.borders
        self.pattern
        self.protection
        
        

```

## 为样式创建字体
```python
import xlwt
style = xlwt.XFStyle()
# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'  # 字体
font.bold = True  # 加粗
font.underline = True  # 下划线
font.italic = True  # 斜体
# 设置样式
style.font = font

```

## 设置列宽
```python
ws.col(0).width = 256 * 20
#width = 256 * 20 256为衡量单位，20表示20个字符宽度

```
## 设置行高
```python

style = xlwt.easyxf('font:height 360;')  # 18pt,类型小初的字号
row = ws.row(0)
row.set_style(style)

```

## 设置边框样式
```python
import xlwt
borders = xlwt.Borders()  # Create Borders
# May be:   NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
#           MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,
#           MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
# DASHED虚线
# NO_LINE没有
# THIN实线

borders.left = xlwt.Borders.DASHED
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

style = xlwt.XFStyle()  # Create Style
style.borders = borders  # Add Borders to Style

```



## 设置单元格背景色
```python
import xlwt
pattern = xlwt.Pattern()

# May be: NO_PATTERN, SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern = xlwt.Pattern.SOLID_PATTERN

# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow,
# 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
# almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray, the list goes on...
pattern.pattern_fore_colour = 5
style = xlwt.XFStyle()
style.pattern = pattern
```




##  设置单元格对齐
```python
import xlwt
al = xlwt.Alignment()
# VERT_TOP = 0x00       上端对齐
# VERT_CENTER = 0x01    居中对齐（垂直方向上）
# VERT_BOTTOM = 0x02    低端对齐
# HORZ_LEFT = 0x01      左端对齐
# HORZ_CENTER = 0x02    居中对齐（水平方向上）
# HORZ_RIGHT = 0x03     右端对齐
al.horz = 0x02  # 设置水平居中
al.vert = 0x01  # 设置垂直居中
style = xlwt.XFStyle()
style.alignment = al

```

## xlrt: 获取单元内容为日期类型的方式

```python

from datetime import datetime,date
 
if sheet1.cell(3,6).ctype == 3 :
    print(sheet1.cell(3, 6).value)  # 41463.0
    date_value = xlrd.xldate_as_tuple(sheet1.cell(3, 6).value, data.datemode)
    print(date_value)  # (2013, 7, 8, 0, 0, 0)
    print(date(*date_value[:3])) # 2013-07-08
    print(date(*date_value[:3]).strftime('%Y/%m/%d'))  # 2013/07/08

```

## 获取整行整列数据
```python

rows = sheet1.nrows
cols = sheet1.ncols

for row in range(rows):
    row_date = sheet1.row_value(row)
    print(row_date)

``` 

