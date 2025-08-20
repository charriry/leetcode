class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n,m = len(matrix),len(matrix[0])
        num = n*m
        result = []
        right,down,left,up = True,False,False,False
        limit_right,limit_down,limit_left,limit_up = m-1,n-1,0,0
        i,j = 0,0  
        while i<=limit_down and j<=limit_right and j>=limit_left and i>= limit_up:
            result.append(matrix[i][j])
            if right == True:
                j += 1
            if down == True:
                i += 1
            if left == True:
                j -= 1
            if up == True:
                i -= 1
            if right and j > limit_right:
                right = False
                down = True
                limit_up += 1
                j -= 1
                i += 1
            if down and i > limit_down:
                down = False
                left = True
                limit_right -= 1
                i -= 1
                j -= 1
            if left and j < limit_left:
                left = False
                up = True
                limit_down -= 1
                j += 1
                i -= 1
            if up and i < limit_up:
                up = False
                right = True
                limit_left += 1
                i += 1
                j += 1
        return result

a = Solution()
matx = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a.spiralOrder(matx))
            


                




