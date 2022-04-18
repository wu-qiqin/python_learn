"""
Created by hu-jinwen on 2022/4/5
"""

for  num in [ 1, 2, 3]:
    print(num)

    if num == 2:
        break
else:
    print("funtional?")

print("end")


# sample:

students = [
    {"name":"xiaohu",
     "age": "18"},
{"name":"xiaowu",
 "age":"18"}
]

find_name = "xiaozhang"

for students_str in students:
    print(students_str)
    if students_str["name"] == find_name:
        print("ok, find you: %s" % find_name)
        break

else:
    print("sorry, i did't find %s" % find_name)

