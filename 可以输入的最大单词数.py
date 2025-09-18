class Solution:
    def canBeTypedWords(self,text:str,brokenLetters:str)->int:
        text = text.split()
        n = len(text)
        i = 0
        broken_set = set()
        for i in range(len(brokenLetters)):
            broken_set.add(brokenLetters[i])
        result = 0
        while i<n:
            m = len(text[i])
            j = 0
            while j<m:
                if text[i][j] in broken_set:
                    break
                if j == m-1:
                    result += 1
                j+=1
            i+=1
            

        return result
    
    #无重复最长子串
    def lengthOfLongestSubstring(self,s:str)->int:
        left = 0
        dict_1 = {}
        i = 0
        result = 0
        while i<len(s):
            if s[i] in dict_1 and dict_1[s[i]] >=left:
                left = dict_1[s[i]]+1
                dict_1[s[i]] = i
            else:
                dict_1[s[i]] = i
            result = max(result,i-left+1)
            i+=1
        return result
    
if __name__ == "__main__":
    a = ""
    b = "ad"
    s = Solution()

    print(s.lengthOfLongestSubstring(a))