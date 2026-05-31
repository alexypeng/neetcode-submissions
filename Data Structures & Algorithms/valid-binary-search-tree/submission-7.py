# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def max_val(node):
            if not node:
                return -1001
            return max(node.val, max_val(node.left), max_val(node.right))
        
        def min_val(node):
            if not node:
                return 1001
            return min(node.val, min_val(node.left), min_val(node.right))

        if not root:
            return True
        if root.val >= min_val(root.right) or root.val <= max_val(root.left):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
