# Given an array of integers temperatures represents the daily temperatures, return an array 
# answer such that answer[i] is the number of days you have to wait after the ith day to get 
# a warmer temperature. If there is no future day for which this is possible, 
# keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = [] 

        for i, temp in enumerate(temperatures):
            
            # The Heatwave Check
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()          # Grabbing the past day from the waiting room
                days_waited = i - index      # Calculating how long it waited
                answer[index] = days_waited  # Writing the answer for That Past day
            
            stack.append(i)

        return answer