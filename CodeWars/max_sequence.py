def max_sequence(arr):
    # 5 kyu
    """
    Easy case is when the list is made up of only positive numbers and the maximum
    sum is the sum of the whole array. If the list is made up of only negative numbers,
    return 0 instead.
    Empty list is considered to have zero greatest sum. Note that the empty list or array
    is also a valid sublist/subarray.
    :param arr:
    :return:
    """

    max_subarray_sum: int = 0
    current_sum: int = 0

    for el in arr:
        current_sum += el
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_subarray_sum:
            max_subarray_sum = current_sum
    return current_sum