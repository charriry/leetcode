class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k < n:
            temp = nums[:n-k]
            del nums[:n-k]
            nums += temp
        else:
            k = k%n




nums = [-1,-100,3,99]
k = 2
a = Solution()
print(a.rotate(nums,k))
print(nums)
