class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        找到一个数组中的第k大的元素
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]
    
    #前k个高频元素
    def topKfrequenct(self,nums,k)->list:
        result = []
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1
        #字典转为堆
        for key,value in dict_nums.items():
            
            heapq.heappush(result,(-value,key))
        ans = []
        for i in range(k):
            value,key = result[0]
            heapq.heappop(result)
            ans.append(key)
        return ans

def MAX_heap(nums:list[int],index):
    n = len(nums)
    left = index*2+1
    right = index*2+2
    largest = index
    if left <n and nums[left]>nums[index]:
        largest = left
    if right<n and nums[right]>nums[largest]:
        largest = right
    if largest != index:
        nums[index],nums[largest] = nums[largest],nums[index]
        MAX_heap(nums,largest)
    


def build_heap(nums:list[int])->list[int]:
    n = len(nums)
    for i in range(n//2,-1,-1):
        MAX_heap(nums,i)
    return nums
import heapq  

if __name__ == "__main__":
    nums = [5,3,1,1,1,3,73,1]
    # k = 2
    # # 构建最大堆，heapq默认是最小堆，所以取相反数实现最大堆
    # max_heap = [-num for num in nums]
    # heapq.heapify(max_heap)
    # res = None
    # for _ in range(k):
    #     res = -heapq.heappop(max_heap)
    # print(res)
    a = Solution()
    print(a.topKfrequenct(nums,k=2))
