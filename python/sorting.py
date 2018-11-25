import pdb

def merge(list1, list2):
    resulting_len = len(list1) + len(list2)
    new_list = []
    while len(new_list) < resulting_len:
        if len(list1) == 0:
            list_removing = list2
        elif len(list2) == 0:
            list_removing = list1
        elif list1[0] < list2[0]:
            list_removing = list1
        else:
            list_removing = list2

        new_list.append(list_removing.pop(0))

    return new_list

assert(merge([], []) == [])
assert(merge([1], []) == [1])
assert(merge([], [2]) == [2])
assert(merge([1], [2]) == [1, 2])
assert(merge([4], [3]) == [3, 4])
assert(merge([5, 7], [3, 9]) == [3, 5, 7, 9])
assert(merge([1], [-1, 0]) == [-1, 0, 1])

def merge_sort(list):
    if len(list) < 2:
        return list
    else:
        divide_point = len(list) // 2

        first_half = list[:divide_point]
        second_half = list[divide_point:]

        list1 = merge_sort(first_half)
        list2 = merge_sort(second_half)

        return merge(list1, list2)

def swap(index1, index2, list):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    return list

def partition(A):
    start_pivot_idx = -1
    final_pivot_idx = 0
    for curr_idx in range(len(A) - 1):
        if A[curr_idx] < A[start_pivot_idx]:
            swap(final_pivot_idx, curr_idx, A)
            final_pivot_idx += 1
    swap(final_pivot_idx, start_pivot_idx, A)
    return final_pivot_idx


def quicksort(A):
    if A == []:
        return []
    q = partition(A)
    A[:q] = quicksort(A[:q])
    A[q+1:] = quicksort(A[q+1:])
    return A


assert(quicksort([]) == [])
assert(quicksort([1]) == [1])
assert(quicksort([999999]) == [999999])
assert(quicksort([919, 7, 8, 3]) == [3, 7, 8, 919])
assert(quicksort([8, 7, 6, 4, 999, 1, 0, -3, -1]) == \
                  [-3, -1, 0, 1, 4, 6, 7, 8, 999])


def get_digit(number, idx):
    num_str = str(num)
    if idx < len(num_str):
        return int()


def insertion_sort(list):
    for i in range(1, len(list)):
        insertion_element = list[i]
        for j in range(i):
            current_sorted_element = list[j]
            if insertion_element < current_sorted_element:
                list[j+1:i+1] = list[j:i]
                list[j] = insertion_element # Could put current_sorted_element?
                break

    return list

assert(insertion_sort([]) == [])
assert(insertion_sort([1]) == [1])
assert(insertion_sort([999999]) == [999999])
assert(insertion_sort([919, 7, 8, 3]) == [3, 7, 8, 919])
assert(insertion_sort([8, 7, 6, 4, 999, 1, 0, -3, -1]) == \
                  [-3, -1, 0, 1, 4, 6, 7, 8, 999])
assert(insertion_sort([9, 8, 7, 6]) == [6, 7, 8, 9])


def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        swap(i, min_index, list)

    return list

assert(selection_sort([]) == [])
assert(selection_sort([1]) == [1])
assert(selection_sort([999999]) == [999999])
assert(selection_sort([919, 7, 8, 3]) == [3, 7, 8, 919])
assert(selection_sort([8, 7, 6, 4, 999, 1, 0, -3, -1]) == \
                  [-3, -1, 0, 1, 4, 6, 7, 8, 999])




# input can be a list of positive integers
# Returns the sorted list

# This sorting algorithm works best on positive integers that are within
# a similar digit length
BASE = 10

def sort_by_place(unsorted, place):
    place_sorted = []

    for digit in range(BASE): # O(BASE)
        for num in unsorted: # O(N)
            num_str = str(num)
            digit_str = str(digit)

            if place > len(num_str):
                if digit == 0:
                    place_sorted.append(num)
                else:
                    continue
            elif num_str[-place] == digit_str:
                place_sorted.append(num)
    return place_sorted

# Assumes elements of list are in the range of 0 to k for some k
def counting_sort(list):
    sorted = len(list) * [0]
    pass

#
# BucketSort
#

# if k is low this algo is fast
# O(K * N)
def radix_sort(unsorted):
    sorted = []

    if unsorted == []:
        return sorted

    max_place = len(str(max(unsorted))) # O(n)
    place = 1
    while place <= max_place: # O(Number of places)
        sorted = sort_by_place(unsorted, place)
        unsorted = sorted.copy()
        place += 1

    return sorted

assert(radix_sort([]) == [])
assert(radix_sort([1]) == [1])
assert(radix_sort([999999]) == [999999])
assert(radix_sort([919, 7, 8, 3]) == [3, 7, 8, 919])
assert(radix_sort([8, 7, 6, 4, 999, 1, 0, 3, 1]) == \
                  [0, 1, 1, 3, 4, 6, 7, 8, 999])
