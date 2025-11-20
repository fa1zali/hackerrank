# Find First Occurrence

# Given a sorted array of integers that may contain duplicates, 
# return the index of the first occurrence of a target value or -1 if not found.

# nums = [1, 2, 3, 4, 5]
# target = 3
# Output = 2

def findFirstOccurrence(nums, target):
    low = 0
    mid = 0
    high = len(nums) - 1
    result_index = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            result_index = mid
            high = mid - 1
    
    return result_index

result = findFirstOccurrence([1, 1, 2, 3, 4, 5], 1)
print(result)