# Check for Non-Identical String Rotation

# Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0.

# s1 = abcde
# s2 = cdeab

# Result: True

# - s2 ('cdeab') is a non-trivial rotation of s1 ('abcde'). 
# - If you rotate 'abcde' left by 2 positions, you get 'cdeab'. 
# - Since s2 is not equal to s1 and is a rotation, the output is true.

def isNonTrivialRotation(s1, s2):

    if len(s1) != len(s2):
        return 0
    elif s1 == s2:
        return 0
    else:
        s1s1 = s1 + s1

        if s2 in s1s1:
            return True
        return 0
    
result = isNonTrivialRotation('abcde', 'cdeab')
print(result)