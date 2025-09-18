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

    def findMin(self,nums:list[int])->int:
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = left+(right-left)//2
            if nums[mid+1] < nums[mid]:
                return mid+1
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        return 0
    def search(self,nums:list[int],target:int)->int:
        """
        查找这个数组中是否有target
        """
        n = len(nums)
        left = 0
        right = n-1
        if n == 0:
            return -1
        while left < right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
        
if __name__ == "__main__":
    a = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(a.search(nums,target))