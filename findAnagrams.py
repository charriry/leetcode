class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n,m = len(s), len(p)
        num_s = [0] * 26
        num_p = [0] * 26
        result = []
        if n < m:
            return result
        for i in range(m):
            num_s[ord(s[i]) - ord('a')] += 1
            num_p[ord(p[i]) - ord('a')] += 1
        if num_s == num_p:
            result.append(0)
        for i in range(m,n):
            num_s[ord(s[i]) - ord('a')] += 1
            #num_p[ord(s[i]) - ord('a')] += 1
            num_s[ord(s[i-m]) - ord('a')] -= 1
            if num_s == num_p:
                result.append(i-m+1)
        return result

        



if __name__ == "__main__":
    a = Solution()
    s = "cbaebabacd"
    p = "abc"
    #print(sorted("acb"))
    print(a.findAnagrams(s,p))