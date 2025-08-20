from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def get_list(head):
    vals = []
    ccur = head
    while ccur:
        vals.append(ccur.val)
        ccur = ccur.next
    return vals
vals = [4,2,1,3]
head = ListNode(0)
ccur = head
for val in vals:
    temp = ListNode(val)
    ccur.next = temp
    ccur = ccur.next
head = head.next

class Solution:
    def findmed(self,head,tail):
        """
        找出中点，划分为两个子链表
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def sort_part(self,head,tail):
        """
        
        """
        med = self.findmed(head,tail)
        if not head or head==tail:
            return head
        temp = med.next
        med.next = None
        return self.merge(self.sort_part(head,med),self.sort_part(temp,tail)) 
    
    def merge(self,list1,list2):
        #合并两个有序链表
        head = ListNode(0)
        ccur = head
        while list1 and list2:
            if list1.val < list2.val:
                ccur.next = list1
                ccur = list1
                list1 = list1.next
            else:
                ccur.next = list2
                ccur = list2
                list2 = list2.next
            #ccur = ccur.next
        if not list1:
            ccur.next = list2
        if not list2:
            ccur.next = list1
        return head.next #返回合并后的头节点
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 找中点前驱
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # 断开链表

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

a = Solution()
print(get_list(a.sortList(head)))