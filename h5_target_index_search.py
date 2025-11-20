# Target Index Search

# Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found.

# nums = [1, 2, 3, 4, 5]
# target = 3
# output = 2


def binarySearch(nums, target):
    low = 0
    mid = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

result = binarySearch([1, 2, 3, 4, 5], 3)
print(result)