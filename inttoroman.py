class Solution:
    def intToRoman(self, num: int) -> str:
        i = 4
        result = ""
        while i>0:
            if num //10**(i-1) == 0:
                i -= 1
                continue
            else:
                num_i = num //10**(i-1)%10
                if num_i <4:
                    if i == 4:
                        result_i = "M"*num_i
                    elif i == 3:
                        result_i = "C"*num_i
                    elif i == 2:
                        result_i = "X"*num_i
                    elif i == 1:
                        result_i = "I"*num_i
                elif num_i == 4:
                    if i == 3:
                        result_i = "C"+"D"
                    elif i == 2:
                        result_i = "X"+"L"
                    elif i ==1:
                        result_i = "I"+"V"
                elif num_i == 5:
                    if i == 3:
                        result_i = "D"
                    elif i == 2:
                        result_i = "L"
                    elif i ==1:
                        result_i = "V"
                elif num_i >5 and num_i < 9:
                    if i == 3:
                        result_i = "D"+"C"*(num_i-5)
                    elif i == 2:
                        result_i = "L"+"X"*(num_i-5)
                    elif i ==1:
                        result_i = "V"+"I"*(num_i-5)
                elif num_i == 9:
                    if i == 3:
                        result_i = "C"+"M"
                    elif i == 2:
                        result_i = "X"+"C"
                    elif i ==1:
                        result_i = "I"+"X"
                i -= 1

                result += result_i
        return result
if __name__ == "__main__":
    a = Solution()
    print(a.intToRoman(100))
