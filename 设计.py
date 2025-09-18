import heapq
class TaskManager:
    """
    设计任务管理器，有添加，执行，修改，删除等方法
    利用小根堆
    """
    def __init__(self,tasks:list[list[int]]):
        self.taskinfo = {} 
        self.heap = [] #for exec
        self.taskid = set()
        for data in tasks:
            self.taskinfo[data[1]] = [data[0],data[1]]
            self.heap.append(((-data[2],-data[0]),data))
            self.taskid.add(data[1])
        heapq.heapify(self.heap)


    def add(self,userId:int,taskId:int,priority:int):
        """
        更新优先级，
        """
        item = [userId,taskId,priority]
        heapq.heappush( self.heap,((-item[2],-item[0]),item) )
        self.taskinfo[taskId] = [userId,priority]
        self.taskid.add(taskId)


    def edit(self,taskId:int,newPriority:int):
        """
        重新编辑taskId的优先级
        """
        self.taskinfo[taskId][1] = newPriority
        #change heap
        for i in range(len(self.heap)):
            prio,data = self.heap[i]
            if data[1] == taskId:
                self.heap.pop(i)
                break
        heapq.heapify(self.heap)
        data = [self.taskinfo[taskId][0],taskId,newPriority]
        heapq.heappush(self.heap,((-data[2],-data[0]),data))

    def rmv(self,taskId:int)->None:
        """
        删除任务
        """
        del self.taskinfo[taskId]
        self.taskid.remove(taskId)


    def execTop(self)->int:
        """
        执行优先级最高的任务，返回任务所属userId,
        """
        while True:
            _,temp = heapq.heappop(self.heap)
            if temp[1] in self.taskid:
                taskId = temp[1]
                del self.taskinfo[taskId]
                self.taskid.remove(taskId)
                return temp[0]
            
if __name__ ==  "__main__":
    first = [[10,4,10],[10,0,6],[5,23,50],[3,29,50],[2,15,9]]
    a = TaskManager(first)
    print(a.execTop())
    print(a.taskinfo,a.heap)
