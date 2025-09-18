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
        """
        判断s是否可以由wordDict中的单词组成
        """
        #判断wordDict中是否有可以由其他元素表示的单词，有的话删去

        word_set = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
    
    #最长递增子序列长度
    def lengthOfLTS(self,nums:list[int])->int:
        n = len(nums)
        max_len = 1
        for i in range(n):
            temp_len = 1
            last = nums[i]
            for j in range(i+1,n):
                if nums[j] > last:
                    temp_len += 1
                    last = nums[j]
                else:
                    continue
            max_len = max(max_len,temp_len)

        return max_len
    
    #乘积最大子数组
    def maxProduct(self,nums:list[int])->int:
        n = len(nums)
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        for i in range(1,n):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            ans = max(ans, max_product)
        return ans
    
    #分隔等和子集
    def canPartition(self,nums:list[int])->bool:
        n = len(nums)
        child_set = []
        target = sum(nums)/2
        if n<2 or sum(nums)%2 == 1:
            return False
        result = False
        def dfs(i):
            nonlocal result
            if i == n:
                return 
            for j in range(i,n):
                child_set.append(nums[i])
                if result:
                    break
                if sum(child_set) == target:
                    result = True
                dfs(j+1)
                child_set.pop()
        dfs(0)
        return result
    
    def uniquePaths(self,m,n):
        i,j = 0,0
        result = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[m-1][n-1]
    
    #最长有效括号
    def longestValidParentheses(self,s:str)->int:
        n = len(s)
        i=0
        left = 0
        longest_dis = 0
        temp = 0
        while i<n:
            if left == 0 and s[i] == ")":
                longest_dis = max(longest_dis,temp)
                i+= 1
                continue
            if s[i] == "(":
                left += 1
                i+=1
                continue
            else:
                left -= 1
                temp+=2
                i+=1
                if left == 0:
                    longest_dis = max(temp,longest_dis)
        
        return max(temp,longest_dis)
    
    #最长公共子序列
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(0,n):
            for j in range(0,m):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

        return dp[n][m]

import heapq
if __name__ == "__main__":
    # a = Solution()
    # text1 = "oxcs"
    # text2 = "shmtox"
    # print(a.longestCommonSubsequence(text1,text2))
    diccs = [1,2,3]
    print("source",diccs)
    diccs.
    print("after",diccs)
import heapq
heapq.heapify   
