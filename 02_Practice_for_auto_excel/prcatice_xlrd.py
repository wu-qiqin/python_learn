"""
Created by hu-jinwen on 2022/5/15
"""
import json


class KBDProductItem(object):
    """"""

    __slots__ = [
        "car_model",
        "customer_id",
        "kbd_id",
        "specification",
    ]

    def __init__(self):
        """"""
        # 车型
        self.car_model = None
        # 客户名号
        self.customer_id = None
        # kbd品号
        self.kbd_id = None
        # 规格
        self.specification = None

    def __str__(self) -> str:
        """"""
        result = {}
        for key in self.__slots__:
            value = self.__getattribute__(key)
            result[key] = value
        return json.dumps(result)

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == '__main__':
    """"""
    import xlrd

    workbook = xlrd.open_workbook("器件涨价清单汽大众.xls")
    sheet1 = workbook.sheet_by_index(1)
    # sheet = workbook.sheet_names()
    # rows_values = sheet1.row_values(0)
    rows = sheet1.get_rows()

    row_list = []

    for row in rows:
        col1 = row[2]
        col2 = row[6]
        col3 = row[7]

        item = KBDProductItem()
        item.kbd_id = col1.value
        item.car_model = col2.value
        item.customer_id = col3.value

        row_list.append(item)

    print(row_list)
