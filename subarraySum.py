class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        dict1 = {"0":1}
        n = len(nums)
        result = 0
        sum_num = 0
        for i in range(n):
            sum_num += nums[i]
            if f'{sum_num-k}' in dict1.keys():
                result += dict1[f'{sum_num-k}']
            dict1[f'{sum_num}'] = dict1.get(f"{sum_num}",0) + 1
            
        return result



