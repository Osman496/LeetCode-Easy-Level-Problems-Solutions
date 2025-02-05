# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

#Solution:

# Approach:
# Sets in Python:

# A set is a data structure that stores unique elements. If you convert a list to a set, any duplicate elements in the list will be removed because sets cannot contain duplicates.

# Logic:

# If the length of the original list (nums) is not equal to the length of the set created from the list (set(nums)), it means there were duplicate elements in the list (since the set removed them).

# If the lengths are equal, it means there were no duplicates.

# Return the Result:

# Return True if duplicates exist (i.e., len(nums) != len(set(nums))).

# Return False if no duplicates exist.

def ContainsDupicate(nums):
    # Compare the length of the list to the length of the set created from the list
    # If they are not equal, it means there are duplicates in the list
    return len(nums) != len(set(nums))

# Example usage:
print(ContainsDupicate([1, 2, 3, 1]))  # Output: True