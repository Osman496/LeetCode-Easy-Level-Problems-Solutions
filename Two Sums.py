# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]




def twoSum(nums, target):
    # Finds the indices of two numbers in the given `nums` array that add up to the `target` value.
    
    # This function uses a dictionary `prevNums` to keep track of the numbers and their indices seen so far. For each number in the `nums` array, it calculates the difference between the `target` and the current number. If that difference has been seen before, the function returns the indices of the two numbers. Otherwise, it adds the current number and its index to the `prevNums` dictionary.
    
    # If no two numbers in the `nums` array add up to the `target`, the function returns `None`.
    prevNums = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in prevNums:
            return [prevNums[diff], index]
        prevNums[num] = index
    return None

print(twoSum([2, 7, 11, 15], 9))  # [0, 1]