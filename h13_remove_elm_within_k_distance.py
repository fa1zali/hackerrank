# Remove Elements Within K Distance

# Given a non-decreasing array of integers and an integer K, 
# remove in-place any element that is within K of the previous 
# kept element and return the new length. Use constant extra space and single pass with two pointers.

# timestamps = [1, 2, 3, 8, 10]
# K = 3

# Output = 2

def k_dist(timestamps, k):

    if len(timestamps)==0:
        return 0
    
    size = 1
    last = timestamps[0]
    
    for i in range(1, len(timestamps)): 
        if (timestamps[i]-last) >= k: 
            timestamps[size]=timestamps[i]
            last=timestamps[i]
            size+=1
    
    return size

result = k_dist([1, 2, 3, 8, 10], 3)
print(result)