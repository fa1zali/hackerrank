# Maximum Number of Non-Overlapping Intervals

# Given an array of intervals where each interval has a start and end time, 
# return the maximum number of non-overlapping intervals.

# meetings = [[1, 2], [2, 3], [3, 4], [1, 3]]
# output = 3

def maximizeNonOverlappingMeetings(meetings):
    meetings.sort(key = lambda x: x[1])
    count = 0
    last_end_time = float('-inf')

    for start,end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count

result = maximizeNonOverlappingMeetings([[0, 5], [0, 1], [1, 2], [2, 3], [3, 5], [4, 6]])
print(result)