class Solution:
    def resultingString(self, s: str) -> str:
        i = 0
        result = ""
        n = len(s)
        j = i+1
        while i<n and j<n:
            if abs(ord(s[i])-ord(s[j]))==1 or abs(ord(s[i])-ord(s[j]))==25:
                if j == n-1:
                    return result
                m = len(result)
                result = result[:m-1]
                s = s[:i]+s[j+1:]
                i = max(i-1,0)
                j = i+1
                n = len(s)
            else:
                result += s[i]
                if j == n-1:
                    result += s[j]
                i += 1
                j += 1
        if len(s) <= 1:
            return s
                
        return result

a = Solution()
print(a.resultingString("abc"))