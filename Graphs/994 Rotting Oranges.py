# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this 
# is impossible, return -1.

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
# because rotting only happens 4-directionally.

import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])
        queue = collections.deque()
        fresh_count = 0
        minutes = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # Counting how many rotten are there at minute 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh_count+=1
                elif grid[r][c]==2:
                    queue.append((r,c))

        while queue and fresh_count > 0:
            level_size = len(queue)
            
            for _ in range(level_size):
                curr_r, curr_c = queue.popleft()
                
                # Looking at the 4 neighbors to check for next round which will rot 
                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    
                    # If neighbor is in bounds and it is a fresh orange (1)
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == 1):
                        
                        grid[new_r][new_c] = 2          # Rot it
                        queue.append((new_r, new_c))    # Adding to queue
                        fresh_count -= 1                # Decrementing the fresh count
                        
            minutes += 1

        if fresh_count==0: return minutes 
        else :return  -1