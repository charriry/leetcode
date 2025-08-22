class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        找到一个数组中的第k大的元素
        """
        if k>len(nums):
            return -1
        
        stack = [nums[0]]*k
        i = 0
        for num in nums:
            if num>stack[i]:
                temp = stack[i]
                str

