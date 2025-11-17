# Count Elements Greater Than Previous Average

# Given an array of positive integers, return the number of elements that are strictly 
# greater than the average of all previous elements. Skip the first element.

# responseTimes = [100, 200, 150,300] >>> 2

# - Day 0: 100 (no previous days, skip) 
# - Day 1: 200 > average(100) = 100 → count = 1 
# - Day 2: 150 vs average(100, 200) = 150 → not greater → count = 1 
# - Day 3: 300 > average(100, 200, 150)

def previous_average(nums):
    size = len(nums)
    sum = 0
    count = 0

    for i in range(size):
        if i == 0:
            continue
        else:
            sum += nums[i-1]

            if nums[i] > (sum/i):
                count += 1
    
    return count



result = previous_average([100, 200, 150,300])
print(result)