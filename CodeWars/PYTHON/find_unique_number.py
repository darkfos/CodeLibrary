"""
    There is an array with some numbers. All numbers are equal except for one. Try to find it!
    It’s guaranteed that array contains at least 3 numbers.
    The tests contain some very huge arrays, so think about performance.
"""

# 1 Решение
# def find_uniq(arr):
#     #6 kyu
#     # your code here
#
#     dct: dict = {arr.count(i): i
#         for i in arr
#     }
#
#     n = dct.get(min(dct))
#     return n   # n: unique number in the array

# 3 Решение
# def find_uniq(arr):
#     #6 kyu
#     # your code here
#     for i in arr:
#         if arr.count(i) == 1:
#             return i


# 2 Решение
# def find_uniq(arr):
#     #6 kyu
#     # your code here
#
#     n = list(filter(lambda x: arr.count(x) == 1, arr))
#     return n[0]   # n: unique number in the array


#Финальное решение
def find_uniq(arr):
    #6 kyu
    set_arr = set(arr)
    for arg in set_arr:
        if arr.count(arg) == 1: return arg

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))