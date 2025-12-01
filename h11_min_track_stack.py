# Min-Tracking Stack Implementation

# Implement a stack that supports push, pop, top, and getMin operations in O(1) time, 
# where getMin returns the minimum element.

# n = 10
# operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']

# Output = [0,0,0,0]

def processCouponStackOperations(operations):
    # Write your code here
    main_stack = []
    min_stack = []
    result = []

    for operation in operations:
        if " " in operation:
            command = operation.split(" ")
        else:
            command = operation
        
        if command[0] == "push":
            val = command[1]
            main_stack.append(val)

            if not min_stack or val <= min_stack[-1]:
                min_stack.append(val)
        
        elif len(main_stack) > 0:

            if command == 'pop':
                if main_stack:
                    if main_stack[-1] == min_stack[-1]:
                        min_stack.pop()
                    main_stack.pop()
            
            if command == 'top':
                if main_stack:
                    result.append(main_stack[-1])
            
            if command == 'getMin':
                if min_stack:
                    result.append(min_stack[-1])

    return result


operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']
result = processCouponStackOperations(operations)
print(result)