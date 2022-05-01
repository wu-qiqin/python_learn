"""
Created by hu-jinwen on 2022/4/19
"""


class Women:
    # 私有属性或者私有：__
    # 私有属性或者私有处理方法：__类名__
    def __init__(self, name):
        self.name = name
        self.__age = 18

    # 在对象的方法内部可以访问对象的私有属性
    def secret(self):
        print("%s 的年龄是  %d" % (self.name, self.__age))


xiaofang = Women('小芳')

# 私有属性在外界不能够被直接访问
#print(xiaofang.age)
# 私有方法在外界也同样不能够被直接访问
xiaofang.secret()
