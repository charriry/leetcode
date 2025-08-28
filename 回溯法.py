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
    
    #组合总和
    def combinationSum(self,candidates:list[int],target:int)->list[list[int]]:
        """
        枚举
        """
        n = len(candidates)
        candidates.sort()
        result = []
        temp = []
        total = 0
        def dfs(i):
            nonlocal total
            if total > target:
                return
            elif total == target:
                result.append(temp[:])
            else:
                for j in range(i,n):
                    temp.append(candidates[j])
                    total += candidates[j]
                    dfs(j)
                    total -= candidates[j]
                    temp.pop()
        dfs(0)
        return result
    
    #括号生成
    def generateparenthesis(self,n:int)->list[str]:
        result = []
        dict_1 = {}
        for i in range(n):
            dict_1[i] = 0
        def code_trans(dict_1):
            result = ""
            for i in range(len(dict_1)):
                temp = "("
                temp += ")"*dict_1[i]
                result += temp
            return result
        def dfs(i):
            
            if i == n:
                target = code_trans(dict_1)
                #if target not in result:
                result.append(target)
                return

            for j in range(i,n):
                if dict_1[j] <= j and j < num_dfs:
                    dict_1[j] += 1
                    dfs(i+1)
                    dict_1[j] -= 1

        dfs(0)
        return result
    
    #单词搜索
    def exist(self,board:list[list[str]],word:str)->bool:
        m,n = len(board),len(board[0])
        s = len(word)
        i,j = 0,0
        index = 0
        def dfs(index,i,j):
            """
            查找word中第i个字母的存在
            """
            if index == s-1:
                return True
            
            #向上
            if i-1>=0 and board[i-1][j] == word[index+1]:
                temp = board[i-1][j]
                board[i-1][j] = "0"
                if dfs(index+1,i-1,j):
                    return True
                board[i-1][j] = temp
            #向下
            if i+1<m and board[i+1][j] == word[index+1]:
                temp = board[i+1][j]
                board[i+1][j] = "0"
                if dfs(index+1,i+1,j):
                    return True
                board[i+1][j] = temp
            #向左
            if j-1>=0 and board[i][j-1] == word[index+1]:
                temp = board[i][j-1]
                board[i][j-1] = "0"
                if dfs(index+1,i,j-1):
                    return True
                board[i][j-1] = temp
            #向右
            if j+1<n and board[i][j+1] == word[index+1]:
                temp = board[i][j+1]
                board[i][j+1] = "0"
                if dfs(index+1,i,j+1):
                    return True
                board[i][j+1] = temp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = "0"
                    if dfs(0,i,j):
                        return True
                    board[i][j] = temp
        return False
    

    #分隔回文串
    def partition(slef,s:str)->list[list[str]]:
        result = []#定义一个结果
        n = len(s)
        temp = []
        def judge(i,j):
            while i<j:
                if s[i] != j:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(index):
            if index == n:
                result.append(temp[:])
                return
            
            for j in range(index,n):
                if judge(index,j):
                    temp.append(s[index:j+1])
                    dfs(j+1)
                    temp.pop()
        dfs(0)        
        return result

    #N皇后
    def solveNQueen(self,n:int)->list[list[str]]:
        result= [["."]*n for _ in range(n)]
        ans = []
        def check(i,j):
            #检查第i行第j列是否可以放置皇后
            #检查列
            if i==0:
                return True
            for k in range(i):
                if result[k][j] == "Q":
                    return False
            #检查斜线
            row = i-1
            delta = 1
            while row>=0:
                if (j-delta>=0 and result[row][j-delta] == "Q") or ( j+delta<n and result[row][j+delta] == "Q"):
                    return False
                row -= 1
                delta += 1
            return True

        def dfs(index):
            """
            表示第i个皇后可以放的位置
            """
            if index == n:
                temp = [''.join(row) for row in result]
                ans.append(temp[:])
                return
            for j in range(n):
                if check(index,j):
                    result[index][j] = "Q"
                    dfs(index+1)
                    result[index][j] = "."

        dfs(0)
        return ans



if __name__ == "__main__":
    a = Solution()

    print(a.solveNQueen(5))