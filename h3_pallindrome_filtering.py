# Check Palindrome by Filtering Non-Letters

# Given a string containing letters, digits, and symbols, determine if it reads the same forwards 
# and backwards when considering only alphabetic characters (case-insensitive).

# code = A1b2B!a >> 1

# - Step 1: Extract only letters → ['A','b','B','a'] 
# - Step 2: Convert to lowercase → ['a','b','b','a'] 
# - Step 3: Compare sequence forward and backward: 'abba' == 'abba' → true

def check_pallindrome(code):

    str = ''
    rev_str = ''

    for elm in code:
        if elm.isalpha():
            str += elm.lower()
    
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i]

    if str == rev_str:
        return True

    return False

result = check_pallindrome('A1b2B!a')
print(result)