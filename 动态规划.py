class Solution:
    def climbStairs(self, n: int) -> int:
        """
        爬楼梯，每次一到两阶，共n阶
        """
        p,q,r = 0,0,1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r
    def generate(self,numRows:int)->list[list[int]]:
        """
        杨辉三角
        """
        result = []
        up_layer = [1]
        if numRows == 1:
            result.append(up_layer)
            return result
        for i in range(numRows):
            #当前层数为i+1
            result.append(up_layer[:])
            up_layer.insert(0,0)
            up_layer.insert(len(up_layer),0)
            temp = [0]*(i+2)
            for j in range(i+2):
                temp[j] = up_layer[j] + up_layer[j+1]
            up_layer = temp
        return result
    
    #打家劫舍
    def rob(self,nums:list[int])->int:
        n = len(nums)
        if n <2:
            return nums[0]
        temp1 = nums[0]
        temp2 = max(nums[0],nums[1])
        #val_set[1] = max(nums[0],nums[1])
        ans = 0
        for i in range(2,n):
            ans = max( temp1 + nums[i] , temp2 )
            temp1 = temp2
            temp2 = ans
        return ans
    
    #完全平方数
    #返回和为n的完全平方数的最小数量
    def numSquares(self,n:int)->int:

        temp = n-7
        for i in range(1,40):
            if n == i**2:
                return 1
            if n > i**2:
                residual = n-(i)**2
                j = 1
                while j<i:
                    if residual == j**2:
                        return 2
                    j += 1
            else:
                break
            k = 0
            while k<5:
                m = 0
                if n<4**k*7:
                    break
                while m < 10:
                    if n == 4**k*(8*m+7):
                        return 4
                    if n<4**k*(8*m+7):
                        break
                    m += 1
                k+=1
        return 3
    
    def coinChange(self,coins:list[int],amount:int)->int:
        """
        返回所需最少得硬币数量
        """
        if amount<= 0:
            return 0
        dp = [float("inf")]*(amount+1)
        for coin in coins:
            dp[coin] = 1

        return dp[amount] if dp[amount]!=float("inf") else -1
    
    #单词拆分
    def wordBreak(self,s:str,wordDict:list[str])->bool:
        n = len(s)
        m = len(wordDict)
        if len(s) == 0:
            return True
        
        def dfs(i):
            """
            定义为到第i个字符串仍可以被表示
            """
            if i == 0:
                return 
            if dfs(i-1):
                return True
            
        return dfs(m)



    
if __name__ == "__main__":
    a = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaababaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
    print(a.wordBreak(s,wordDict))
    #print(s)
    #print(a.coinChange(coins=coin,amount=100))
