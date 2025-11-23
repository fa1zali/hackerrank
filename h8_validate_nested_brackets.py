# Validate Properly Nested Brackets

# Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. 
# Return 1 if valid, otherwise return 0. 
# 
# snippet = if (a[0] > b[1]) { doSomething(); } 
# Output = 1 
# 
# constraints: 
# 0 <= code_snippet.length <= 1000 '
# code_snippet consists of printable ASCII characters (character codes 32 to 126 inclusive) 
# code_snippet may contain any combination of '(', ')', '{', '}', '[', ']', letters, digits, symbols, and whitespace 
# code_snippet may be empty

# Stack Approach (Time Complexity: O(n), Space Complexity: O(n))
def pnb(snippet):

    if len(snippet) == 0:
        return 0
    
    pairs = {')': '(', '}': '{', ']': '['}

    stack = []

    for char in snippet:

        if char in '[{(':
            stack.append(char)
        
        elif char in ']})':
            if not stack:
                return 0
            
            if stack[-1] == pairs[char]:
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0
    
snippet = "if (a[0] > b[1]) { doSomething(); }"

result = pnb(snippet)
print(result)

            