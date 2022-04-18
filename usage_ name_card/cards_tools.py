"""
Created by hu-jinwen on 2022/4/5
"""
card_list = []


def show_menu():
    print("*" * 30)
    print("welcome to use name card system")
    print("")
    print("1: adding new card")
    print("2: show all inf")
    print("3: searching card")
    print("")
    print("0: exit system")
    print("*" * 30)


def new_card():
    print("-" * 30)
    print("adding new card")

    # 提示输入用户输入名片信息
    name_str = input("please adding your name:")
    phone_str = input("please adding your phone number:")
    qq_str = input("please adding your qq number:")
    email_str = input("please adding your email:")

    # 使用用户输入的信息建立一个名片字典

    card_dic = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str}

    # 将名片字典添加到列表中
    card_list.append(card_dic)
    print(card_list)

    # 提示用户添加成功

    print("creat a new name card: %s" % name_str)


def show_all():
    print("-" * 30)
    print("show all inf")

    # 判断是否存在记录
    if len(card_list) == 0:
        print("no records , please adding new inf :")

        # return  可以返回一个函数的执行结果
        # 下方代码不会被执行
        # 如果return 后面没有任何的内容，表示回返回调用函数的位置
        # 并且不返回任何结果

        return

    # 打印表头
    for x in ["name", "phone", "qq", "email"]:
        print(x, end="\t\t")
    print("")

    # 打印分隔线
    print("*" * 30)

    # 遍历名片列表输出字典信息
    for card_dic in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dic["name"],
                                            card_dic["phone"],
                                            card_dic["qq"],
                                            card_dic["email"]))


def search():
    print("-" * 30)
    print("searching card")

    # 提示用户输入姓名
    find_name = input("please key your name")

    # 遍历名片列表 如果没有找到，提示用户输入
    for card_dic in card_list:
        if card_dic["name"] == find_name:
            print("name\t\t phone\t\t qq\t\t email")
            print("*" * 30)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dic["name"],
                                                card_dic["phone"],
                                                card_dic["qq"],
                                                card_dic["email"]))

            deal_card(card_dic)

            break
    else:
        print("sorry, no useful inf %s:" % find_name)


def deal_card(find_name):
    """

    :param find_name: 文件名
    :return:
    """
    print(find_name)

    option_str = input("please choose your option:"
                       " [1] change [2] delete [0] back to previous menu")

    if option_str == "1":
        find_name["name"] = input("name: ")
        find_name["phone"] = input("phone ")
        find_name["qq"] = input("qq: ")
        find_name["email"] = input("email: ")

        print("change name card")

    elif option_str == "2":
        card_list.remove(find_name)

        print("delete successfully !")

# 课程到 222 课-225课 skip
# 跳课到 226 课

