"""
Created by hu-jinwen on 2022/4/4
"""
info_tuple = ("zhangsan", 18, 1.75, 18, 1.88)

x = info_tuple[1]

print(x)

empty_tuple = ()
meaning =type(empty_tuple)

single_tuple = (5,)
meaning_02 =  type(single_tuple)
print(meaning_02)

print(meaning)
print(empty_tuple)

print(info_tuple.index(18))
print(info_tuple[0])
print(info_tuple.count(18))
print(len(info_tuple))


