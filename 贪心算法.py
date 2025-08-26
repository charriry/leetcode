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
    
if __name__ == "__main__":
    price = [7,1,5,3,6,4]
    a = Solution()
    print(a.maxProfit(price))