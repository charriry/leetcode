class Solution:
    def judge(self,s):
        if ord(s)<=90 and ord(s)>=65:
            return True
        elif ord(s)<=122 and ord(s)>=97:
            return True
        else:
            return False
    #小写字母改为大写字母
    def change(s):
        if ord(s)<=122 and ord(s)>=97:
            return chr(ord(s)-32)
        else:
            return s
    #大写字母转为小写字母
    def change2(s):
        if ord(s)<=90 and ord(s)>=65:
            return chr(ord(s)+32)
        else:
            return s
    def generateTag(self,caption:str)->str:
        result = ''
        result += '#'
        n = len(caption)
        IF_FIRST = True
        n = max(100,n)
        print(caption[0])
        for i in range(n):
            if self.judge(caption[i]):
                if IF_FIRST:
                    result += self.change(caption[i])
                else:
                    result += self.change2(caption[i])
            else:
                continue
   
        return result
if __name__ == '__main__':
    s = Solution()
    print(s.judge('H'))
    print(s.generateTag('Hello World!'))  # 输出: #HELLO WORLD!