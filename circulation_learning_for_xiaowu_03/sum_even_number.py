"""
Created by hu-jinwen on 2022/4/3
"""
i = 0
result = 0

while i <= 100:
    if i % 2 == 0:
        result += i

    i = i + 1

print("sum result from 0 to 100 is %d" % result )

