class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums = sorted(nums)
        label = 0
        for i in range(len(nums)):
            if nums[i]>0:
                label = i
                break
        for i in range(0,label):
            if i>2 and nums[i] == nums[i-2]:
                continue
            for j in range(i+1,len(nums)):
                if nums[j] == nums[j-1] or nums[i] == nums[j] :
                    continue
                sum_2 = -(nums[i]+nums[j])
                left = max(label,j+1)
                if sum_2 in nums[left:]:
                    temp = [nums[i],nums[j],sum_2]
                    result.append(temp)
        
        return result
if __name__ == "__main__":
    a = Solution()
    nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
    print(a.threeSum(nums))