class Solution:
    def maxArea(self, height: list[int]) -> int:
        def Volumn(i,j):
            return (j-i)*min(height[i],height[j])
        l,r = 0,len(height)-1
        i = 1
        left,right = 0,len(height)-1
        for i in range(1,len(height)-1):
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            if Volumn(l,r) > Volumn(left,right):
                left,right = l,r
        return Volumn(left,right)

            
if __name__ == "__main__":
    height = [5,2,12,1,5,3,4,11,9,4]
    a = Solution()
    print(a.maxArea(height))