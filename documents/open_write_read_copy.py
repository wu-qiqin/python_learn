"""
Created by hu-jinwen on 2022/4/25
"""
# 打开文件
file_read = open("content")
file_write = open("content[copy]", "w")


# 读写
while True:
    #读取一行内容

    text = file_read.readline()
# 判断是否读取到内容
    if not text:
        break

    file_write.write(text)


# 关闭
file_write.close()
file_read.close()