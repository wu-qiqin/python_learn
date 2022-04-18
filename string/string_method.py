"""
Created by hu-jinwen on 2022/4/5
"""

# space
hello_string = "hello world "

print( hello_string.isspace())

# start
print(hello_string.startswith("hello"))



#end
print(hello_string.endswith("world "))


#find

print(hello_string.find("lloo"))
print(hello_string.index("llo"))

#repalce : not change the origin str

print(hello_string.replace("hello","hi"))

print(hello_string)

