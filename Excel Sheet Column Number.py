# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701


class Solution(object):
    def titleToNumber(self, columnTitle):
        # Initialize the column number to 0
        columnNumber = 0
        # Loop through each character in the columnTitle
        for i in range(len(columnTitle)):
            # Multiply the current column number by 26 to shift to the next place in base-26
            # Add the value of the current character, calculated as (ord(char) - ord('A') + 1)
            columnNumber = columnNumber * 26 +(ord(columnTitle[i]) - ord('A') + 1)
        return columnNumber
    
print(Solution().titleToNumber("A")) #1
print(Solution().titleToNumber("AB")) #28
print(Solution().titleToNumber("ZY")) #701