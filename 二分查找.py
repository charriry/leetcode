class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        mid = n//2
        reminder = n % 2
        #ans = mid
        if nums[0] > target:
            return 0
        if nums[-1] <target:
            return n
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid],target)
        else:
            return self.searchInsert(nums[mid+1:],target) + mid + n %2
        
    #在排序数组中查找元素的第一个和最后一个位置
    def searchRange(self,nums:list[int],target:int)->list[int]:
        n = len(nums)
        result = []
        start = n-1
        end = 0
        left = 0
        right = n-1
        #先寻找起始位置
        while right-left>0:
            mid = (right+left)//2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        if n<=0 or nums[left] != target:
            result.append(-1)
        else:
            result.append(nums[left])
        left = 0
        right = n-1
        while right-left>1:
            mid = (right+left)//2
            if nums[mid] == target:
                left = mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        if n<=0 or nums[left] != target:
            result.append(-1)
        else:
            result.append(left)
        return result
        
        




        
if __name__ == "__main__":
    a = Solution()
    nums = [5,7,7,8,8,10]
    target = 6
    print(a.searchRange(nums,target))