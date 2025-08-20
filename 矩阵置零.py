class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        col_set = set()
        while i<n:
            change = False
            j = 0
            while j<m:
                if matrix[i][j] != 0:
                    
                    if j in col_set:
                        matrix[i][j] =0
                    j += 1
                    continue
                else:
                    change = True#这一行遍历后再转为0
                    col_set.add(j)
                    for k in range(i):
                        matrix[k][j] = 0 #将上面的同列转为0
                j += 1
            if change == True:
                matrix[i] = [0]*m
            i += 1
            





matr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
a = Solution()
a.setZeroes(matr)
print(matr)

