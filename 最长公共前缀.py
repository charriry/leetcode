class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        min_len = min(len(_) for _ in strs)
        num_str = len(strs)
        
        for i in range(min_len):
            for j in range(len(strs)-1):
                if strs[j][i] == strs[j+1][i]:
                    if j == len(strs)-2:
                        result += strs[0][i]
                    continue
                else:
                    return result
        return result
    
if __name__ == "__main__":
    a = Solution()
    str_1 = ["flower","flow","flight"]
    print(a.longestCommonPrefix(str_1))