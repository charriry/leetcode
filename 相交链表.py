class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # 当两个指针不同时为None时循环
        while pA is not pB:
            # 如果pA到达末尾，转到headB；否则继续下一个
            pA = pA.next if pA else headB
            # 如果pB到达末尾，转到headA；否则继续下一个
            pB = pB.next if pB else headA
        
        # 如果相交，返回交点；否则返回None
        return pA

# 主函数用于测试
def main():
    # 创建公共部分
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    # 创建链表A: 4 -> 1 -> 8 -> 4 -> 5
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common
    
    # 创建链表B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common
    
    solution = Solution()
    intersection = solution.getIntersectionNode(headA, headB)
    
    if intersection:
        print("相交节点的值为:", intersection.val)
    else:
        print("两个链表不相交")

if __name__ == "__main__":
    main()