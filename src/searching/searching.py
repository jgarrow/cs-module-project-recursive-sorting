# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    lowest = start
    highest = end
    middle = lowest + ((highest - lowest) // 2)

    # if list is empty, return -1
    if end < 0 or start < 0:
        return -1
    
    elif arr[middle] == target:
        return middle
    elif arr[middle] < target:
        lowest = middle
    elif arr[middle] > target:
        highest = middle
    
    return binary_search(arr[lowest: highest], target, lowest, highest)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

