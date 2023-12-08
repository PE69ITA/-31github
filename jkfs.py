class Solution:
    def numIslands(self, grid):
        def islandsConverter(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                islandsConverter(i + 1, j)
                islandsConverter(i - 1, j)
                islandsConverter(i, j + 1)
                islandsConverter(i, j - 1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    islandsConverter(i, j)
        return counter

# Example usage:
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

solution = Solution()
result = solution.numIslands(grid)

print(result)  # Output: 1
