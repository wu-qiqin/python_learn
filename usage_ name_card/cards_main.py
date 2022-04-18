"""
Created by hu-jinwen on 2022/4/5
"""

import cards_tools

# 无限循环
while True:

    # TODO （xiaohu） 显示功能菜单
    cards_tools.show_menu()

    action_str = input("please choose your option:")
    print("you chose: %s" % action_str)

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()

        elif action_str == "2":
            cards_tools.show_all()

        elif action_str == "3":
            cards_tools.search()

    elif action_str == "0":
        print("welcome to use name_card system again!")
        break

    else:
        print("please chose again!")
