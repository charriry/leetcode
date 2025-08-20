class Solution:
    def merge(self,intervals:list[list[int]])->list[list[int]]:
        """
        合并区间
        """
        result = []
        intervals = sorted(intervals,key=lambda s:s[0])
        left = intervals[0][0]
        temp = intervals[0][1]
        residue = False
        for i in range(len(intervals)):
            if i == len(intervals)-1:
                if residue:
                    temp = max(temp,intervals[i][1])
                    result.append([left,temp])
                else:
                    result.append(intervals[i])
                break
            if intervals[i+1][0] <= temp:
                temp = max(temp,intervals[i+1][1])
                residue = True
                continue
            else:
                result.append([left,temp])
                left = intervals[i+1][0]
                temp = intervals[i+1][1]
                residue = False
        return result
a = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(a.merge(intervals))
