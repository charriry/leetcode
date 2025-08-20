class Solution:

    def isMatch(self,s: str, p: str)  ->bool:# 正则表达式匹配
        def match(s_idx, p_idx):
            if s_idx == 0 and p_idx == 0:
                return True
            if p_idx == 0:
                return False
            if s_idx == 0:
                if p[p_idx-1] == "*":
                    return match(s_idx, p_idx - 2)
                else:
                    return False
            if p[p_idx - 1] != "*":
                return (s[s_idx - 1] == p[p_idx - 1] or p[p_idx - 1] == ".") and match(s_idx - 1, p_idx - 1)
            else:
                if s[s_idx - 1] == p[p_idx - 2] or p[p_idx - 2] == ".":
                    return match(s_idx - 1, p_idx) or match(s_idx, p_idx - 2)
                else:
                    return match(s_idx, p_idx - 2)

        l1, l2 = len(s),len(p)
        #p = [[False]*(l2+1) for _ in range(l1+1)]
        #p[0][0] = True

        return match(l1,l2)
if __name__ == "__main__":
    s = "aaa"
    p = "aaaa*"
    a = Solution()
    print(a.isMatch(s,p))