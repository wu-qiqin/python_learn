## 类属性

```python

A： 使用赋值语句，定义类属性

B： 类属性给类对象中定义的属性，用于记录类的特征，不记录具体对象特征：

C: 举例：

class Tool(object):
    count = 1

    def __init__(self, name):
        Tool.count += 1


D： 访问类属性方法：
01 ： 类名.类属性
02 ： 对象.类属性（不推荐）



```