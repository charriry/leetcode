
def calc_value(s:str)->int:
    ans = 0
    zero_num = s.count("0")
    one_num = s.count("1")
    n = len(s)
    if zero_num > one_num:
        ans = (zero_num*(zero_num+1))/2
        if s[-1] == "1":
            temp = 0
            for j in range(n-1,0,-1):
                if s[j] == "1":
                    temp += 1
                    ans += temp
                else:
                    break
        if s[0] == "1":
            temp = 0
            for j in range(0,n-1):
                if s[j] == "0":
                    temp += 1
                    ans += temp
                else:
                    break
    elif zero_num < one_num:
        ans = (one_num*(one_num+1))/2
        if s[-1] == "0":
            temp = 0
            for j in range(n-1,0,-1):
                if s[j] == "0":
                    temp += 1
                    ans += temp
                else:
                    break
        if s[0] == "0":
            temp = 0
            for j in range(0,n-1):
                if s[j] == "0":
                    temp += 1
                    ans += temp
                else:
                    break
    else:
        ans = (one_num*(one_num+1))/2 + 1
         
    return int(ans)
if __name__ == "__main__":
    n = 100
    s = "0011010101101110110010000001001110110010010110111111110111010110010111001000001001110000111111011110"
    result = calc_value(s)
    print(result)