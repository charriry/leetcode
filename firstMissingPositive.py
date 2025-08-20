class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            """
            原地哈希将值放在索引对应的位置
            """
            while 0 <= nums[i] <= n and nums[nums[i]-1 ] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n
a = Solution()
nums = [2,2,2,1,0]
print(a.firstMissingPositive(nums))