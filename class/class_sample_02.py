"""
Created by hu-jinwen on 2022/4/17
"""
"""
摆放家具

房子：户型 总面积 家具（新房子无家具）

家具： 家具名称 占地面积
床：4平
衣柜：2平
餐桌：1.5平

需要输出：户型 总面积 剩余面积 家具列表

"""


class HouseItem:
    def __init__(self, item_name, occupied_area):
        self.item_name = item_name
        self.occupied_area = occupied_area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.item_name, self.occupied_area)


class House:
    def __init__(self, house_type, total_area):
        self.house_type = house_type
        self.total_area = total_area

        self.free_area = total_area
        self.item_list = []

    def __str__(self):

        return ("户型%s\n总面积:%.2f 剩余面积:%2.f\n家具：%s"
                % (self.house_type,self.total_area,
                   self.free_area,self.item_list ))

    def add_item(self, item):
        # 1. 判断新家具占地面积
        if item.occupied_area > self.free_area:
            print("%s 面积太大，无法添加" % item.name)
            return
        # 2. 将新家具的她添加到家具列表中
        self.item_list.append(item)

        # 3. 计算剩余面积
        self.free_area -= item.occupied_area

        print("add %s" % item)
        pass


# 创建家具
bed = HouseItem("bed", 4)
chest = HouseItem("chest", 2)
table = HouseItem("table", 1.5)

print(bed)
print(chest)
print(table)


# 创建房子
my_home = House("两室一厅", 70)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)