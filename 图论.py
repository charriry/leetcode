class Solution:
    #岛屿数量，最少有一个岛屿
    def numIslands(self, grid: list[list[str]]) -> int:
        def change_ele(row,col):
            grid[row][col] = "0"
        def dfs(row,col):
            if row==len(grid) or col== len(grid[0]) or grid[row][col] == "0":
                return
            elif row == -1 or col == -1:
                return
            else:
                change_ele(row,col)
                dfs(row+1,col)
                dfs(row,col+1)
                dfs(row-1,col)
                dfs(row,col-1)
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans

a = Solution()
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(a.numIslands(grid))


