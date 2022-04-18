"""
Created by hu-jinwen on 2022/4/2
"""

age_1 = input("please key your age:")
age = int(age_1)
print(type(age_1))
if age >= 18:
    print("you are  am adult.")
elif age< 14:
    print("you are a child")
else:
    print("you are a teenager")
