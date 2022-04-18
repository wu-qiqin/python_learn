"""
Created by hu-jinwen on 2022/4/4
"""

xiaohu = {"name": "xiaohu",
          "age": "18",
          "gender": "male",
          "height": "180"}

print(xiaohu)
# getting inf
print( xiaohu["age"])


# adding inf
xiaohu["weight"] = 140


# modification inf
xiaohu["name"] = "xiaowu"

# pop inf
xiaohu.pop("name")

# len
print(len(xiaohu))

# conbine
temp_dic = {"marriage": "single",
            "age": "20"}
xiaohu.update(temp_dic)

# clear
xiaohu.clear()

print(xiaohu)