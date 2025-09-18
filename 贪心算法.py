class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0]*n
        min_val = prices[0]
        max_pri = 0
        for i in range(1,n):
            max_pri = max(0,prices[i]-min_val,max_pri)
            min_val = min(min_val,prices[i])
        return max_pri
    
    #跳跃游戏
    def canJump(self,nums:list[int])->bool:
        """
        跟踪当前能到达的最远位置
        """
        n = len(nums)
        i = 0
        longest_dis = 0
        while i<n-1:
            if longest_dis >= n-1:
                return True
            longest_dis = max(longest_dis,i+nums[i])
            i +=1
        return False
    
    #跳跃游戏2(最小步数)
    def jump(self,nums:list[int])->int:
        res = 0
        n = len(nums)
        if n<2:
            return 0
        i = 0
        while i<n:
            res += 1
            temp_dis = i + nums[i]
            if temp_dis>=n-1:
                return res
            max_dis = i
            for j in range(i+1,temp_dis+1):
                val = nums[j] +j
                if nums[j] +j >=n-1:
                    return res+1
                if val>=max_dis:
                    max_dis = val
                    arise = j
            i = arise
        return res
    
    #划分字母区间
    def partitionLabels(self,s:str)->list[int]:
        res = []
        dict_1 = {}
        for i in range(len(s)):
            dict_1[s[i]]  = dict_1.get(s[i],0)+1
        i = 0
        stack = {}
        temp = 0
        while i<len(s):
            stack[s[i]] = stack.get(s[i],0)+1
            if stack[s[i]] == dict_1[s[i]]:
                del stack[s[i]]
            if not stack:
                res.append(i+1-temp)
                temp = i+1
            i += 1
        return res


        
from collections import defaultdict
if __name__ == "__main__":
    s = "caedbdedda"
    a = Solution()
    print(s[0])
    print(a.partitionLabels(s))