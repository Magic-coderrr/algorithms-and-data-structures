# ou are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
# return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfit(prices):
    left = 0  # Buy pointer
    right = 1 # Sell pointer
    max_profit = 0 
    
    while right < len(prices):
        
        # We found a profitable window
        if prices[left] < prices[right]:
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
            
        # We found a cheaper price. 
        else:
            # update the left pointer to this new low price
            left = right
            
        right += 1
        
    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
