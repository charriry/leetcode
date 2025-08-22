class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #matrix_T = matrix.T
        #row = 0
        def findinarr(arr,target):
            #二分查找目标
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False


        def binary_search(left,right,target):
            if right-left == 1:
                return findinarr(matrix[left],target)
            if right - left == 0:
                return False
            mid = (right + left) // 2
            if target < matrix[mid][0]:
                return binary_search(left, mid, target)
            elif target > matrix[mid][-1]:
                return binary_search(mid+1,right, target)
            else:
                return findinarr(matrix[mid], target)
        return binary_search(0,len(matrix), target)


        
            
matrix = [[1],[3]]
target = 4
a = Solution()
print(a.searchMatrix(matrix,target))