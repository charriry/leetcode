class Solution:
    def find_j(self,i,j):
        if i==j*2:
            return True
        else:
            return False
    def find_k(self,i,k):
        if i == k:
            return True
        else:
            return False
    def specialTriplets(self, nums: list[int]) -> int:
        total_num=0
        n = len(nums)
        j_finded = False
        for i in range(n):
            j_num = 0
            for j in range(i+1,n):
                if j_finded and self.find_k(nums[i],nums[j]):
                    #j_finded = False
                    if total_num +j_num-1 == 1e-9+6:
                        total_num = j_num-1
                    else:
                        total_num += j_num
                    
                elif j_finded and self.find_j(nums[i],nums[j]):
                    j_num += 1
                elif self.find_j(nums[i],nums[j]):
                    j_finded = True
                    j_num += 1
        return total_num
    
if __name__ == "__main__":
    a = Solution()
    nums = [46,54,0,23,46,69,15,0,0,30]
    print(a.specialTriplets(nums))
    