# def tes1t():
#     print('aaa')
#     p=yield '123'
#     print('bbb')
#     k=yield '321'
#
# a=tes1t()
# print(next(a)) #第一次执打印aaa  123  第二次打印bbb  321，执行第一yield迭代暂停，行
# print(next(a))

#
# def yield_test(n):
#     if n >10:
#         return "太大了"
#     else:
#         print('yield的用法')
#         while n<= 10:
#
#             yield n
#             n-=1
#             if n <0:
#                 return
#         return "pass"
#
#
# d=yield_test(10)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


# def a():
#
#     print('aaa')
#
#     p = yield '123'
#
#     print('bbb')
#
#     k = yield '234'
#
# r = a()
#
# print(next(r))

