import heapq
class MinStack:
    
    def __init__(self):
        self.stack = [] #保留输入顺序
        self.minheap = []#最小堆结构
        self.removed = {} #删除的元素

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minheap, val)
        self.removed[val] = self.removed.get(val, 0) + 1 #val值被放置了removed[val]次

    def pop(self) -> None:
        temp= self.stack.pop()
        self.removed[temp] -= 1
    def getMin(self) -> int:
        while self.minheap and self.removed.get(self.minheap[0], 0) == 0: #如果最小值的放置次数为0，就弹出最小值
            heapq.heappop(self.minheap)
        return self.minheap[0]

    def top(self) -> int:
        return self.stack[-1]


class Solution:
    def decodeString(self,s:str):
        result = ""
        temp_num = 0
        num_stack = []
        str_stack = []
        for ch in s:
            if ord(ch)<=57 and ord(ch)>=48:
                temp_num = temp_num*10+int(ch)
                continue
            elif ch =="[":
                num_stack.append(temp_num)
                str_stack.append("")
                temp_num = 0
                continue
            elif ch == "]":
                temp_str = str_stack.pop()*num_stack.pop()
                if not num_stack:
                    result += temp_str
                else:
                    str_stack[-1] += temp_str
                continue
            else:
                if not num_stack:
                    result += ch
                else:
                    str_stack[-1] += ch
        return result
    
    #每日温度
    def dailyTemperatures(self,temperatures:list[int])->list[int]:
        res = [0]*len(temperatures)
        stack = []
        n = len(temperatures)
        i = 0
        while i<n:
            temp = temperatures[i]
            while stack:
                top_index,top_value = stack[-1]
                if temp>top_value:
                    res[top_index] = i-top_index
                    stack.pop()
                else:
                    stack.append((i,temp))
                    break
            if not stack:
                stack.append((i,temp)) 
            i += 1
        return res

    # 柱状图中最大的矩形
    def largestRectangleArea(self,heights:list[int])->int:
        """
        单调栈
        :param heights:
        :return:
        """
        #找出以h(i)为高的左右边界，再计算最大值
        n = len(heights)
        left = [-1]*n
        right = [n]*n
        stack = []
        max_area = 0
        for i in range(n):
            while stack:
                if heights[i] > heights[stack[-1]]:
                    left[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    temp = stack.pop(-1)
                    max_area = max(max_area,heights[temp]*(i-left[temp]-1))
            if not stack:
                stack.append(i)
                continue
        while stack:
            temp = stack.pop(-1)
            max_area = max(max_area,heights[temp]*(n-left[temp]-1))

        return max_area


            

a = Solution()
s = [6,7,5,2,4,5,9,3]
print(a.largestRectangleArea(s))