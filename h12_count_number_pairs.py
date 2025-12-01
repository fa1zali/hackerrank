# Count Number Pairs

# Given a sorted array of positive integers and a target value,
# count the number of pairs (i, j) where i < j and array[i] + array[j] <= target.

# def count_number_pairs(arr, target):

#     count = 0

#     for i in range(len(arr)):
#         for j in range(len(arr)):

#             if i<j and i!=j and arr[i] + arr[j] <= target:
#                 count += 1

#     return count

def count_number_pairs(arr, target):

    count = 0
    l = 0
    r = len(arr) - 1

    while l < r:

        if arr[l] + arr[r] <= target:
            count += r - l
            l += 1
        else:
            r -= 1

    return count

prices = [1, 2, 3, 4, 5]
budget = 7
print(count_number_pairs(prices, budget))
