class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = 0
        if (m+n)%2 == 0:
            k = (m+n)//2+1
        else:
            k = (m+n)//2
        while k > 0:
            index = k//2-1
            if nums1[index] <= nums2[index]:
                nums1 = nums1[index:]
                k -= index
            else:
                nums2 = nums1[index:]
                k -= index


        
        return result
    


if __name__ == "__main__":
    lists1 = [1,2]
    lists2 = [-1,3]
    a = Solution()
    print(a.findMedianSortedArrays(lists1,lists2))
