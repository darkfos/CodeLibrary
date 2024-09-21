"""
    Your task is to rotate a matrix 90 degree to the left.
    The matrix is an array of integers with dimension n,m. So this kata checks some basics, it's not too difficult.

    There's nothing more to explain, no tricks, no "bad cases";-). Perhaps you take a look at the testcases...
"""


def rotate_matrix(arr):
    #7 kyu

    new_arr: list = []
    indx = -1
    local_arr: list = []
    for j in range(len(arr[0])):
        for i in arr:
            local_arr.append(i[indx])
        new_arr.append(local_arr)
        local_arr = []
        indx -= 1

    return new_arr