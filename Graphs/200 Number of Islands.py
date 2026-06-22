# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
#  return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally 
# or vertically. You may assume all four edges of the grid are all surrounded by water.
# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

import collections

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
            
        visited = set()
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def bfs(r, c):
            queue = collections.deque([(r, c)])
            visited.add((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        grid[new_r][new_c] == "1" and 
                        (new_r, new_c) not in visited):
                        
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        # Running the outer loop to scan the grid
        for r in range(rows):
            for c in range(cols):
                # We only call bfs if we find new land
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)           # Mapping out the whole island
                    island_count += 1   

        return island_count