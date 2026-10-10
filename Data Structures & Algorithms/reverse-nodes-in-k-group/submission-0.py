# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_end = dummy

        while True:
            kth = self.getKth(prev_end, k)
            if not kth:
                break
            nxt = kth.next

            prev, curr = kth.next, prev_end.next
            while curr != nxt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_end.next
            prev_end.next = kth
            prev_end = tmp
        return dummy.next
