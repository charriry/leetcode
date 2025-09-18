from collections import defaultdict
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
    
    #腐烂的橘子
    def orangesRotting(self,grid:list[list[int]])->int:
        num_one = 0
        num_two = 0
        start_list = []
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == 1:
                    num_one += 1
                if col == 2:
                    start_list.append((i,j))
                    num_two+=1
        if num_one == 0:
            return 0
        if num_two == 0:
            return -1
        i = 0

        def every_minute(start_list,grid,num_one):
            new_start_list = []
            for i,j in start_list:
                if i>0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    new_start_list.append((i-1,j))
                    num_one -= 1
                if i<len(grid)-1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    new_start_list.append((i+1,j))
                    num_one -= 1
                if j>0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    new_start_list.append((i,j-1))
                    num_one -= 1
                if j<len(grid[0])-1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    new_start_list.append((i,j+1))
                    num_one -= 1
            return new_start_list,num_one

        while num_one>0:
            temp_list,temp_one = every_minute(start_list,grid,num_one)
            if num_one == temp_one:
                return -1
            start_list,num_one = temp_list,temp_one
            i += 1
        return i

    #课程表
    def canFinish(self,numCourses:int,prerequisites:list[list[int]])->bool:
        edges = defaultdict(list)
        valid = True
        visited = [0]*numCourses
        search_set = set()
        for info in prerequisites:
            search_set.add(info[1])
            search_set.add(info[0])
            edges[info[1]].append(info[0])
        
        def dfs(u):
            visited[u] = 1
            nonlocal valid
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            
            visited[u] = 2

        for i in search_set:
            if valid and not visited[i]:
                dfs(i)
        return valid

a = Solution()
numcourses = 17

dict_1 = {}
dict_1[1] = [2,3]
print(dict_1[1])