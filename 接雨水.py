class Solution:
    def trap(self,height:list[int])->int:
        """
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        """
        n = len(height)
        result = 0
        left = [height[0]]
        for i in range(1,n):
            left.append(max(left[i-1],height[i]))
        right = [height[n-1]]
        for i in range(n-2,-1,-1):
            right.append(max(right[n-i-2],height[i]))
        right.reverse()
    
        #对于第i个柱子，可以蓄水的量就是左侧最高的柱子与右侧最高的柱子之中较小者，当然只有较小者也大于第i个柱子的高度
        for i in range(1,n-1):
            value = min(left[i],right[i])
            if value > height[i]:
                result += value-height[i]
        return result



