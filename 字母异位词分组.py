class Solution:
         
    def groupAnagrams(self,strs:list[str])->list[str]:
        result = {}
        for i in range(len(strs)):
            key = ''.join(sorted(list(strs[i])))
            if key not in result:
                result[key] = [strs[i]]
            else:
                result[key].append(strs[i])
        return list(result.values())



        return result
if __name__ == "__main__":
    a = Solution()
    strs = ["vow","pam","vic","bee","ken","jay","oft","sue","joy","yuk","sac","mac","inc","big","icy","bus","lob","flo","day","aol",
            "eel","rex","jug","man","cod","mix","guy","ken","ion","meg","tot","noe","ref","ito","inn","van","cry","tad"]
    print(a.groupAnagrams(strs))
    #print(ord('a'),ord('z'))
