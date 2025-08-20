class Solution:
    def productExceptSelf(self,nums:list[int])->list[int]:
        left = []
        right = []
        result = []
        left.append(1)
        n = len(nums)
        if nums.count(0)>1:
            return [0]*n
        for i in range(1,n):
            left.append(left[i-1]*nums[i-1])
        right.append(1)
        result.append(right[0]*left[n-1])
        for i in range(n-1,0,-1):
            right.append(right[n-i-1]*nums[i])
            result.append(right[n-i]*left[i-1])
        result.reverse()

        return result
        
        
