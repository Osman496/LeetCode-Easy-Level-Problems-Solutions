# 125. Valid Palindrome
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

def is_palindrome(s):
    # Step 1: Convert to lowercase and filter out non-alphanumeric characters
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Step 2: Check if the cleaned string reads the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

print(is_palindrome("dad"))