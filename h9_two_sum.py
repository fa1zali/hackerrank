# Given an array of positive integers and a target integer, 
# return the indices of two elements that sum to the target or [-1, -1] if no such pair exists.

# taskDurations = [2, 7, 11, 15]
# slotLength = 9

# Output = [0, 1]


def findTaskPairForSlot(taskDurations, slotLength):

    map = dict()

    for i in range(len(taskDurations)):

        difference = abs(taskDurations[i] - slotLength)

        if difference in map:

            if i < map[difference]:
                return [i, map[difference]]
            return [map[difference], i]
        
        map[taskDurations[i]] = i

    return [-1, -1]

taskDurations = [2, 7, 11, 15]
slotLength = 9
result = findTaskPairForSlot(taskDurations, slotLength)
print(result)