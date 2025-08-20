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
        
if __name__ == "__main__":
    a = Solution()
    nums = [1,3,6,9]
    target = 9
    print(a.searchInsert(nums,target))