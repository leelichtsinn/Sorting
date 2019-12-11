# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i, j = 0, 0
    while (len(merged_arr) < len(arrA) + len(arrB)):
        if arrA[i] < right[j]:
            merged_arr.append(arrA[i])
            i+=1
        else:
            merged_arr.append(arrB[j])
            j+=1
        if i == len(arrA) or len(arrB):
            merged_arr.extend(arrA[i:] or arrB[j])
            break

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
        return arr

    # find middle of arr
    mid = len(arr) // 2

    # divide arr
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    return merge(left_arr, right_arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
