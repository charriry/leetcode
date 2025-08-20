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
    
if __name__ == "__main__":
    a = Solution()
    n = 1
    print(a.generate(n))
