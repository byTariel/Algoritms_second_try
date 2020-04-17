""" Сформировать из введенного числа обратное по порядку входящих в него цифр
    и вывести на экран. Например, если введено число 3486, надо вывести 6843.
    dz_2_task_3
"""


import timeit
import cProfile
import sys


sys.setrecursionlimit(3010)


# первый вариант (линейная зависмость)
def func_while(n, reverse_n):
    while n > 0:
        reverse_n += str(n % 10)
        n //= 10
    return int(reverse_n)


print(timeit.timeit('func_while(1_000, "")', number=1000, globals=globals()))     # 0.002355145000000003
print(timeit.timeit('func_while(1_000**2, "")', number=1000, globals=globals()))  # 0.004180884999999995
print(timeit.timeit('func_while(1_000**4, "")', number=1000, globals=globals()))  # 0.008526026999999999
print(timeit.timeit('func_while(1_000**8, "")', number=1000, globals=globals()))  # 0.01622206300000001
# так как Х - это строка, то квардратичное увеличении Х,
# в итоге это всего-лишь каждый раз удвоение кол-ва символов в Х
# и при этом увеличение У тоже равномерное, примерно тоже в два раза за шаг

cProfile.run('func_while(1, "")')             # 1    0.000    0.000    0.000    0.000 dz_4_task_1.py:12(func_while)
cProfile.run('func_while(100, "")')           # 1    0.000    0.000    0.000    0.000 dz_4_task_1.py:12(func_while)
cProfile.run('func_while(100_000, "")')       # 1    0.000    0.000    0.000    0.000 dz_4_task_1.py:12(func_while)
cProfile.run('func_while(1_000**1_000, "")')  # 1    0.018    0.018    0.018    0.018 dz_4_task_1.py:12(func_while)
# специально сделал большой скачок, чтобы хоть какое-то изменение увидеть вместо нулей


# # второй вариант (линейная зависмость) !!! самое быстрое !!!
# def func_for(n, reverse_n):
#     n = str(n)
#     for i in n:
#         reverse_n = i + reverse_n
#     return int(reverse_n)
#
#
# print(timeit.timeit('func_for(1_000, "")', number=1000, globals=globals()))     # 0.001337175000000003
# print(timeit.timeit('func_for(1_000**2, "")', number=1000, globals=globals()))  # 0.0018095239999999999
# print(timeit.timeit('func_for(1_000**4, "")', number=1000, globals=globals()))  # 0.0027392109999999983
# print(timeit.timeit('func_for(1_000**8, "")', number=1000, globals=globals()))  # 0.004588974000000003
# # так как Х - это строка, то квардратичное увеличении Х,
# # в итоге это всего-лишь каждый раз удвоение кол-ва символов в Х
# # и при увеличение У примерно в полтора раза за шаг
#
# cProfile.run('func_for(1, "")')             # 1    0.000    0.000    0.000    0.000 dz_4_task_1.py:31(func_for)
# cProfile.run('func_for(100, "")')           # 1    0.000    0.000    0.000    0.000 dz_4_task_1.py:31(func_for)
# cProfile.run('func_for(100_000, "")')       # 1    0.000    0.000    0.000    0.000 dz_4_task_1.py:31(func_for)
# cProfile.run('func_for(1_000**1_000, "")')  # 1    0.002    0.002    0.002    0.002 dz_4_task_1.py:31(func_for)
# # САМЫЙ БЫСТРЫЙ СПОСОБ


# # рекурсия остатков от деления (линейная зависмость)
# def func_cut(n, reverse_n):
#     if n <= 0:
#         return int(reverse_n)
#     return func_cut(n // 10, reverse_n + str(n % 10))
#
#
# print(timeit.timeit('func_cut(1_000, "")', number=1000, globals=globals()))     # 0.0028310980000000006
# print(timeit.timeit('func_cut(1_000**2, "")', number=1000, globals=globals()))  # 0.005227082000000001
# print(timeit.timeit('func_cut(1_000**4, "")', number=1000, globals=globals()))  # 0.009264129999999999
# print(timeit.timeit('func_cut(1_000**8, "")', number=1000, globals=globals()))  # 0.018373914000000005
# # так как Х - это строка, то квардратичное увеличении Х,
# # в итоге это всего-лишь каждый раз удвоение кол-ва символов в Х
# # и при этом увеличение У тоже равномерное, примерно в 1,8 раза за шаг
#
# cProfile.run('func_cut(1, "")')             # 2/1    0.000    0.000    0.000    0.000 dz_4_task_1.py:63(func_cut)
# cProfile.run('func_cut(100, "")')           # 4/1    0.000    0.000    0.000    0.000 dz_4_task_1.py:63(func_cut)
# cProfile.run('func_cut(100_000, "")')       # 7/1    0.000    0.000    0.000    0.000 dz_4_task_1.py:63(func_cut)
# cProfile.run('func_cut(1_000**1_000, "")')  # 3002/1    0.026    0.000    0.026    0.026 dz_4_task_1.py:63(func_cut)


# # рекурсия срезов (линейная зависмость)
# def func_slice(n, reverse_n):
#     n = str(n)
#     if n == '':
#         return int(reverse_n)
#     return func_slice(n[1:], n[0] + reverse_n)
#
#
# print(timeit.timeit('func_slice(1_000, "")', number=1000, globals=globals()))     # 0.003327471999999998
# print(timeit.timeit('func_slice(1_000**2, "")', number=1000, globals=globals()))  # 0.005338189000000004
# print(timeit.timeit('func_slice(1_000**4, "")', number=1000, globals=globals()))  # 0.009868607000000001
# print(timeit.timeit('func_slice(1_000**8, "")', number=1000, globals=globals()))  # 0.017943604000000002
# # так как Х - это строка, то квардратичное увеличении Х,
# # в итоге это всего-лишь каждый раз удвоение кол-ва символов в Х
# # и при этом увеличение У тоже равномерное, примерно в 1,8 раза за шаг
#
# cProfile.run('func_slice(1, "")')             # 2/1    0.000    0.000    0.000    0.000 dz_4_task_1.py:83(func_slice)
# cProfile.run('func_slice(100, "")')           # 4/1    0.000    0.000    0.000    0.000 dz_4_task_1.py:83(func_slice)
# cProfile.run('func_slice(100_000, "")')       # 7/1    0.000    0.000    0.000    0.000 dz_4_task_1.py:83(func_slice)
# cProfile.run('func_slice(1_000**1_000, "")')  # 3002/1    0.011    0.000    0.011    0.011 dz_4_task_1.py:83(func_slice)
# # эта рекурсия в два раза эффективнее предыдущей


def test_func(func):
    checkup = 5001
    assert checkup == func(100500, '')
    print(f'тест ОК')



# test_func(func_slice)
# test_func(func_cut)
# test_func(func_while)
# test_func(func_for)
