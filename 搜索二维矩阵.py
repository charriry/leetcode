class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #result = False
        i,j = 0,0
        m = len(matrix)
        n = len(matrix[0])
        while i < m and j <n:
            if matrix[i][0] > target:
                return False
            if matrix[i][j] > target:
                i += 1 
                n = j
                j = 0
            elif matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                if j == n-1:
                    i += 1
                    j = 0
                else:
                    j += 1
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
a = Solution()
print(a.searchMatrix(matrix,target))