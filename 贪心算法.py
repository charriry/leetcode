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
                

        
        dp = [False]*n
        dp[0] = True
        for i in range(1,n):
            for j in range(i):
                if dp[j] and nums[j] >= i-j:
                    dp[i] = True
                    break
        return dp[n-1]
    
if __name__ == "__main__":
    price = [7,1,5,3,6,4]
    a = Solution()
    print(a.maxProfit(price))