"""
Created by hu-jinwen on 2022/4/5
"""

# 对齐:just
poem = ["登鹳鹊楼",
"王焕之",
"白日依山尽",
"黄河入海流",
"欲穷千里目",
"更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.rjust(10," "))

# 删除空白字符: strip
poem = ["\t\n登鹳鹊楼",
"王焕之",
"白日依山尽",
"黄河入海流\t\n",
"欲穷千里目",
"更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.strip().ljust(10," "))

# split

poem_str = "\t\n登鹳鹊楼\t王焕之\n白日依山尽\r黄河入海流\t\n欲穷千里目\t\n更上一层楼"
print(poem_str)

poem_list = poem_str.split()
print(poem_list)

# join
result = " ".join(poem_list)
print(result)

#切片

num_str = "012344455567889"
print(num_str[2:5])
print(num_str[::2])
print(num_str[1::2])
print(num_str[2:-1:2])
print(num_str[2:-1])
print(num_str[-2:])
print(num_str[0::-1])
print(num_str[-1::-1])
print(num_str[::-1])