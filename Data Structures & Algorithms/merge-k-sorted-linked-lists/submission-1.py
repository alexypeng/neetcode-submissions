# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        heap = []
        res = ListNode()
        cur = res

        for lst in lists:
            if lst:
                heapq.heappush(heap, NodeWrapper(lst))
        
        while heap:
            node_wrapper = heapq.heappop(heap)
            if node_wrapper.node.next:
                heapq.heappush(heap, NodeWrapper(node_wrapper.node.next))
            cur.next = node_wrapper.node
            cur = cur.next
        
        return res.next



        