# Binary Search Implementation in Python (Iterative)
# If the given element is present in the array, it prints the index of the element.
# if the element is not found after traversing the whole array, it will give -1
# Prerequisite : the given array must be a sorted array
# Time Complexity : O(log n)
# Space complexity : O(1)

#defining the iterative function
def binary_search(array: list, n: int):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # checking if n is present at mid
        if array[mid] < n:
            low = mid + 1

        # If n is greater, compare to the right of mid
        elif array[mid] > n:
            high = mid - 1

        # If n is smaller, compared to the left of mid
        else:
            return mid

            # element was not present in the array, return -1 (standard procedure)
    return -1


# example array
array = [2, 3, 4, 10, 12, 24, 32, 39, 40, 45, 50, 54]
n = 3

# calling the binary search function
result = binary_search(array, n)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in given array")
