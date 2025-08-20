class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        l = len(s)
        result = 0
        for i,ch in enumerate(s):
            if i == l-1:
                result += SYMBOL_VALUES[s[i]]
                break
            if i<l-1 and SYMBOL_VALUES[s[i]] >= SYMBOL_VALUES[s[i+1]]:
                result += SYMBOL_VALUES[s[i]]
            else:
                result -= SYMBOL_VALUES[s[i]]
        return result
if __name__ == "__main__":
    a = Solution()
    print(a.romanToInt("IX"))