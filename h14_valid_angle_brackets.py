# Generate Valid Angle Bracket Sequences

# Given n, return all valid sequences of n pairs of '<' and '>' with proper nesting.


# Time Complexity: O(Cn.n) Catalan number
def generateAngleBracketSequences(n):
    result = []
    
    def backtrack(s, open, close):
        
        if len(s) == 2*n:
            result.append(s)
            return
            
        if open < n:
            backtrack(s+'<', open+1, close)
        
        if close < open:
            backtrack(s+'>', open, close+1)
            
    
    backtrack("", 0, 0)
    
    return result

result = generateAngleBracketSequences(n=2)
print(result)