## *「Apps - App - Books - Book - Sheets - Sheet - Range 」**


## 安装 pip install xlwings

```python
# 如下网址里面有xlwings 的详细讲解
https://zhuanlan.zhihu.com/p/120415076

```

## 结构

```python

# 引入库
import xlwings as xw

# 打开Excel程序，默认设置：程序可见，只打开不新建工作薄
# app = xw.Aop () # 创建一个新的工作簿 # （） 内容为自定义设置
app = xw.App(visible=True,add_book=False) 
# 新建工作簿 (如果不接下一条代码的话，Excel只会一闪而过，卖个萌就走了）
wb = app.books.add()

# 打开已有工作簿（支持绝对路径和相对路径
wb = app.books.open('example.xlsx')
#练习的时候建议直接用下面这条
#wb = xw.Book('example.xlsx')
#这样的话就不会频繁打开新的Excel

# 保存工作簿
wb.save('example.xlsx')

#退出工作簿（可省略）
wb.close()

# 退出Excel
app.quit()

```

## App 流程
```python
# 1. 创建App
app=xw.App()

# 2. 查看PID
pid = app.pid

# 3. 引用App
app = xw.apps[1668]
[1668]就是这个App的PID

# 4. 返回当前活动App
app = xw.apps.active


# 5. 激活App
app.activate()
# '传入参数
app.activate(steal_focus=True)


# 6. 退出App
app.kill():通过杀掉进程,强制Excel app退出
app.quit():退出excel程序,不保存任何工作簿

# 7. 重新计算一遍所有工作簿里的公式
app.calculate()

#8. 设置屏幕更新
'返回屏幕更新状态'
app.screen_updating
'关闭屏幕更新'
app.screen_updating = False


# 9. App是否可见设置
'返回App可见性'
app.visible
'设置App为可见'
app.visible = True

# 10. 设置提醒信息是否显示

# 在使用Excel的过程中，经常会遇到一些提醒信息，比如关闭前的保存提示、数据有效性的警告窗口，若想隐藏这些窗口，可进行如下设置
app.display_alerts=False


```

