class Solution:
    def get_index(self,i,j,n):
        return j,n-1-i
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #顺时针将矩阵旋转90°
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp



max1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
a = Solution()
a.rotate(max1)
print(max1)