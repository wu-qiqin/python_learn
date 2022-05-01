"""
Created by hu-jinwen on 2022/4/24
"""
# 打开文件
file_read = open("content")
file_write = open("content[copy]", "w")



# 读写
text = file_read.read()
file_write.write(text)


# 关闭
file_write.close()
file_read.close()

