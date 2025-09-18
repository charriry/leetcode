# Python queue 常用类与方法示例

## 标准库 queue 模块


import queue

# 1. Queue（FIFO队列）
q = queue.Queue(maxsize=5)  # 可选最大长度
q.put(1)
q.put(2)
print(q.get())  # 输出 1
print(q.empty())  # 是否为空
print(q.full())   # 是否已满

# 2. LifoQueue（栈，后进先出）
lq = queue.LifoQueue()
lq.put('a')
lq.put('b')
print(lq.get())  # 输出 'b'

# 3. PriorityQueue（优先队列，最小优先）
pq = queue.PriorityQueue()
pq.put((2, 'low'))
pq.put((1, 'high'))
print(pq.get())  # 输出 (1, 'high')

# 主要方法：
# put(item, block=True, timeout=None)  # 入队
# get(block=True, timeout=None)         # 出队
# empty()                              # 是否为空
# full()                               # 是否已满
# qsize()                              # 当前队列长度


## collections.deque（双端队列，支持队列和栈操作）

from collections import deque

d = deque()
d.append(1)      # 右侧入队
d.appendleft(2)  # 左侧入队
print(d.pop())   # 右侧出队，输出 1
print(d.popleft()) # 左侧出队，输出 2

# 主要方法：
# append(x)         # 右侧入队
# appendleft(x)     # 左侧入队
# pop()             # 右侧出队
# popleft()         # 左侧出队
# extend(iterable)  # 右侧批量入队
# extendleft(iterable) # 左侧批量入队
# rotate(n)         # 旋转队列
# clear()           # 清空

# 适用场景
# queue.Queue 适合多线程安全队列
# collections.deque 适合高效的队列和栈操作
