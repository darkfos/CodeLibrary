"""
    As part of this kata, you need to find the length of the sub-array that begins and ends with the specified number.

    For example, if the array arr is [0, -3, 7, 4, 0, 3, 7, 9], finding the length of the sub-array that
    begins and ends with 7s would return 5.
    For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.
    If there are less or more than two occurrences of the number to search for, return 0.
"""


def length_of_sequence(arr,n):
    #7 kyu

    try:
        if arr.count(n) > 2:
            if len(arr) == 2:
                return len(arr)
            else:
                return 0
            
        first_number: int = arr.index(n)
        last_number: int = max([number for number in range(len(arr)) if arr[number] == n])
        
        if first_number == last_number:
            return 0
        return len(arr[first_number:last_number+1])
    except Exception:
        return 0        