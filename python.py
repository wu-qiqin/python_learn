# d = {"a": 1, "b": 2, "c": 3}
#
# # for n in d:
# #     print(n)
# # for key in d:
# #     print(key)
# # for value in d.values():
# #     print(value)
# # for key in d.keys():
# #     print(key)
# # for n,m in d.items():
# #     print(n,m)
#
#
# # for item in "ABC" :
# #     print(item)
# # from collections.abc import Iterable
# # print(isinstance("abc",iterable))
#
# # a = 1
# # print(isinstance(a,int))
# # print(isinstance(a,str))
# # print(isinstance(a,(str,int,list,tuple)))
#
# # from collections.abc import Iterable
# # print(isinstance(123, Iterable))
#
# # def findMinAndMax(L):
# #     if not isinstance(L, Iterable):
# #         print('类型错误')
# #         return L
# #     min = None
# #     max = None
# #
# #     print(L)
# #     print()
# #     # 拦截空list
# #     if len(L) == 0:
# #         return (min, max)
# #     # 非空操作
# #     min = max = L[0]
# #     # print(min, max)
# #     for i in L:
# #         if i <= min:
# #             min = i
# #         elif i >= max:
# #             max = i
# #         # print(min, max)
# #     return (min, max)
#
#
# # L = []
# # for x in range (1,11):
# #     L.append(x * x)
# # print(L)
# # # print([x * x for x in range(1,15)])
# # print([x*y for x in range(1,10) for y in range(1,2) if x %2==0])
# # l = []
# # for x in range (1,11):
# #     l.append(x*x)
# # print(l)
# #
# # print([m+n for m in "123" for n in "456"])
#
#
# # l = ["friend","name","car"]
# # print([s.upper() for s in l])
# #
# # m = ['FRIEND', 'NAME', 'CAR']
# # print([y.lower() for y in m])
# #
# # L = ['Hello', 'World', 18, 'Apple', None]
# # print([s.lower() for s in L if isinstance(s,str)])
# # print([s.lower() if isinstance(s,str) else s for s in L])
#
# # print([x*x for x in range(1,10)])
# # l = [x*x for x in range(1,20)]
# # print(l)
# # m = (x * x for x in range(1, 20))
# # print(m)
# # for n in m:
# #     print(n)
#
#
# # from collections.abc import Iterable
# # print(isinstance([],Iterable))
# # print(isinstance((),Iterable))
# # print(isinstance("abc",Iterable))
# # print(isinstance(123,Iterable))
#
#
# # from collections.abc import Iterator
# # # print(isinstance(iter([]),Iterator))
# # # print(isinstance((),Iterator))
# # print(isinstance(iter("123"),Iterator))
#
#
# # def abs(x):
# #     if x >0:
# #         return x
# #     else:
# #         return -x
# # print(abs(-9))
#
# # f = abs
# # print(f(-1))
# # print(abs(-7))
#
#
# # def add (a,b,c):
# #     return c(a)+c(b)
# # print(add(5,6,abs))
#
# # def sum (x,y,z):
# #     return z(x)+z(y)
# # print(sum(3,-4,abs))
#
# # def f(x):
# #     return x * x
# # l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # r = map(f, l)
# # print(list(r))
#
# a = []
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def f(n):
#     return n * n
#     for n in l:
#         n.append(f(n))
#
#
# print(f(6))
#
#
# class Restaurant():
#     def __init__(restaurant_name, cuisine_type):
#         """"""


class ExcelOpt(object):
    """"""

    def __init__(self, path):
        """"""

    def open_sheet(self):
        """"""

    def close_excel(self):
        """"""


if __name__ == '__main__':
    """"""
    opt_instance = ExcelOpt(path="***excel_path***")

    sheet = opt_instance.open_sheet()
    opt_instance.close_excel()
