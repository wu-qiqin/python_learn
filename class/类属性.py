"""
Created by hu-jinwen on 2022/4/23
"""


class Tool:
    count = 0

    @classmethod
    def show_class_count (cls):
        print("工具对象的数量是 %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


# 创建工具对象
futou = Tool("斧头")
langtou = Tool("榔头")
chutou = Tool("锄头")

# 输出工具对象的总数
# print(Tool.count)
#通过类名. 调用静态方法，无需创建对接
Tool.show_class_count()