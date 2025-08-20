class Solution:
    def longestConsecutive(self,nums:list[int]):
        longest = 0
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                continue
            else:
                current_long = 1
                #NEXT_EXIST = True
                while True:
                    if num+1 in nums:
                        num = num+1
                        current_long += 1
                        continue
                    else:
                        longest = max(longest,current_long)
                        break
        return longest
    
if __name__ == "__main__":
    a = [1,1,2]
    b = [2,2,3]
    del a[0]
    print(a+b)