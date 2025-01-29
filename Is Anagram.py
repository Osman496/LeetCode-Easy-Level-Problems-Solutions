# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Anagram: Strings that contain the same characters with the same frequencies.

# First loop: Counts character frequencies in s.

# Second loop: Counts character frequencies in t.

# Comparison: If the dictionaries are equal, the strings are anagrams (True); otherwise, they are not (False).



class Solution:
    class Anagram:
        def isanagram(s,t):
            if len(s) != len(t):
                return False
            countS, countT = {}, {}
            
            for char in s:
                countS[char] = countS.get(char,0) + 1
            for char in t:
                countT[char] = countT.get(char,0) + 1

            return countS == countT
        
print(Solution.Anagram.isanagram("anagram","nagaram"))
print(Solution.Anagram.isanagram("rat","car"))


#2nd Way of doing this
def isAnagram(s,t):
    return len(s) == len(t) and sorted(s) == sorted(t)
print(isAnagram("anagram", "nagaram")) # True
