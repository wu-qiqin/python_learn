"""
Created by hu-jinwen on 2022/4/4
"""
name_list = ["xiaowu", "xiaohu", "xiaoyuan", "zhuzhu"]

list_len = len (name_list)
print("how many items appeared: %d" %list_len)

count = name_list.count("xiaohu")
print("how many times: %d" % count)

name_list.remove("xiaohu")

print(name_list)
