#!/usr/bin/python3
def find_peak(list_of_integers):
    """
    This function finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
