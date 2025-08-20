import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        window_now = nums[:k]
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        result.append(-q[0][0])
        for i in range(k,n):
            heapq.heappush(q, (-nums[i], i))#时间复杂度log(n)
            while q[0][1] <= i - k:
                heapq.heappop(q)#时间复杂度o(log(n))
            result.append(-q[0][0])
        return result

if __name__ == "__main__":
    a = Solution()
    nums = list(map(int,input().split(',')))
    k = int(input())
    # sleep(100)  # Removed or comment out if not needed
    print(a.maxSlidingWindow(nums,k))