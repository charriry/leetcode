class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #matrix_T = matrix.T
        #row = 0
        def findinarr(arr,target):
            mid = len(arr) // 2
            if mid == 0:
                return arr[0] == target
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                return findinarr(arr[:mid], target)
            else:
                return findinarr(arr[mid+1:], target) 

        def binary_search(left,right,target):
            if len(martix) == 1:
                return findinarr(martix[0],target)
            if not martix:
                return False
            mid = len(martix) // 2
            if target < martix[mid][0]:
                return binary_search(martix[:mid], target)
            elif target > martix[mid][-1]:
                return binary_search(martix[mid+1:], target)
            else:
                return findinarr(martix[mid], target)
        return binary_search(matrix, target)


        
            
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 5
a = Solution()
print(a.searchMatrix(matrix,target))