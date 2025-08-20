class Solution:
    #全排列
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        def backsort(start):
            if start == n:
                result.append(nums[:])
            for i in range(start,n):
                nums[start],nums[i] = nums[i],nums[start]
                backsort(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        backsort(0)
        return result
    
    # 子集
    def subsets(self,nums:list[int])->list[list[int]]:
        """
        枚举
        """
        result = []
        temp = []
        def dfs(start):
            result.append(temp[:])

            for i in range(start,len(nums)):
                #新增值
                temp.append(nums[i])
                #递归
                dfs(i+1)
                #回溯
                temp.pop()
        dfs(0)
        return result
    
    #电话号码的字母组合
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []
        temp = []
        def backtrack(index):
            if index == len(digits):
                result.append(''.join(temp))
                return 
            num = digits[index]
            for char in phone_map[num]:
                temp.append(char)
                backtrack(index + 1)
                temp.pop()
        backtrack(0)
        return result

if __name__ == "__main__":
    a = Solution()
    number = "23"
    print(a.letterCombinations(number))