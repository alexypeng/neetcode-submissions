# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        heap = []
        counter = 0

        for lst in lists:
            while lst:
                heapq.heappush(heap, (lst.val, counter, lst))
                counter += 1
                lst = lst.next

        while heap:
            node = heapq.heappop(heap)
            res.next = node[2]
            res = res.next
        
        return dummy.next
