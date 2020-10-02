# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    # elements = len(left) + len(right)
    # merged_arr = [0] * elements

    # Your code here

    left_index, right_index = 0, 0
    result = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # add the greater values that are leftover after we've reached the end of one of the arrays
    result += left[left_index:]
    result += right[right_index:]
    return result

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) <= 1:
        return arr

    middle_index = len(arr) // 2

    left = merge_sort(arr[:middle_index])
    right = merge_sort(arr[middle_index:])

    # if we've divided the original array down to arrays that are either empty or have 1 thing, we can start merging them
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

