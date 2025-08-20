class Solution:
    def judge(self,dict1,dict2):
        for key in dict2:
            if key not in dict1 or dict2[key] > dict1[key]:
                return False
        return True
    def minWindow(self,s:str,t:str)->str:
        result = []
        
        n,m = len(s),len(t)
        minlen = n+1
        if n<m:
            return ""
        target_dict = {}
        window_dict = {}
        for i in range(m):
            if t[i] in target_dict:
                target_dict[t[i]] += 1
            else:
                target_dict[t[i]] = 1
            if s[i] in window_dict:
                window_dict[s[i]] += 1
            else:
                window_dict[s[i]] = 1
        if n<m:
            return result
        i,j = 0,m
        if window_dict == target_dict:
            result = s[:m]
            return result
        while j<n+1:
            if self.judge(window_dict,target_dict):
                if j-i < minlen:
                    result = [i,j]
                    minlen = min(minlen,j-i)
                window_dict[s[i]] -= 1
                i += 1
            else:
                if j<n and s[j] in window_dict:
                    window_dict[s[j]] += 1
                else:
                    if j<n:
                        window_dict[s[j]] = 1
                j += 1
        if len(result) == 0:
            return ""
        else: 
            return s[result[0]:result[1]]


                    



if __name__ =="__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    b = {"a":1,"b":2}
    for key in b:
        print(b[key])
    # print(b.keys())
    a = Solution()
    print(a.minWindow(s,t))

