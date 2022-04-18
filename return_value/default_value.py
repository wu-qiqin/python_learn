"""
Created by hu-jinwen on 2022/4/16
"""


def students_inf(name, gender=True):
    """

    :param name: 班级学生姓名
    :param gender: ture 男生 false 女生
    """
    gender_text = "male"
    if not gender:
        gender_text = "female"

    print("%s is %s" % (name, gender_text))


students_inf("xiaohu")
students_inf("xiaowu", gender=False)