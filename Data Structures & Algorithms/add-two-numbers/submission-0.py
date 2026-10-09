# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            cur1.val += cur2.val
            if cur1.val > 9:
                cur1.val -= 10
                if cur1.next:
                    cur1.next.val += 1
                else:
                    cur1.next = ListNode(1)
            cur1 = cur1.next
            cur2 = cur2.next
        
        if cur2:
            cur1.next = cur2
        
        return l1