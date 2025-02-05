# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

#Soltuion

# Approach:
# Two Pointers:

# left: Represents the day we buy the stock.

# right: Represents the day we sell the stock.

# Iterate Through Prices:

# The right pointer moves forward every iteration to explore potential selling days.

# If the price at left is less than the price at right, it means we can make a profit by buying at left and selling at right. We calculate the profit and update max_profit if this profit is greater than the current max_profit.

# If the price at left is greater than or equal to the price at right, it means we found a better (lower) buying price at right. So, we move the left pointer to right to consider buying at this new lower price.

# Return the Result:

# After iterating through all the prices, return the max_profit.



class Solution(object):
    def maxProfit(self, prices):
        # Initialize two pointers:
        # left = buy day, right = sell day
        left, right = 0, 1
        # Initialize max_profit to 0
        max_profit = 0
        
        # Iterate through the prices using the right pointer
        while right < len(prices):
            # If the price at left is less than the price at right,
            # it means we can make a profit by buying at left and selling at right
            if prices[left] < prices[right]:
                # Calculate the profit and update max_profit if this profit is greater
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                # If the price at left is greater than or equal to the price at right,
                # move the left pointer to right to consider buying at this new lower price
                left = right
            # Move the right pointer forward to explore the next selling day
            right += 1
        
        # Return the maximum profit found
        return max_profit

# Example usage:
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5