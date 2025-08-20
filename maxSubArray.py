class Solution:
    def maxSubarray(self,nums):
        """
        消耗内存大
        """
        n = len(nums)
        i = 0
        sum_left = 0
        max_value = max(nums)
        if max_value <= 0:
            return max_value
        while i<n:
            if nums[i] <= 0 and sum_left == 0:
                i += 1
                continue
            else:
                sum_left += nums[i]
                max_value = max(max_value,sum_left)
                if sum_left <= 0:
                    sum_left = 0
                i += 1
        return max_value

a = Solution()
nums = [3,-2,-3,-3,1,3,0]
print(a.maxSubarray(nums))