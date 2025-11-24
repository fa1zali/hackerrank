# Given two strings s and t, return 1 if t is an anagram of s, otherwise return 0.

# s = listen
# t = silent
# Output = 1

def isAnagram(s, t):

    if len(s) != len(t):
        return 0

    frequency = [0] * 26

    def char_to_index(letter):
        return ord(letter) - ord('a')

    for i in range(len(s)):
        frequency[char_to_index(s[i])] += 1
        frequency[char_to_index(t[i])] -= 1

    for i in range(len(frequency)):
        if frequency[i] != 0:
            return 0
    return 1

s = "listen"
t = "silent"

result = isAnagram(s, t)
print(result)