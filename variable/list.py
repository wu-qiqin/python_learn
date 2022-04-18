"""
Created by hu-jinwen on 2022/4/4
"""
name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[1])

print(name_list.index("wangwu"))
name_list[2] = "wangmazi"


name_list.append("husansan")
name_list.insert(2,"xiaohuhu")

temp_list = ["001", "002", "003"]
name_list.extend(temp_list)



name_list.remove("001")
name_list.pop()
name_list.pop(3)
name_list.clear()


print(name_list)



