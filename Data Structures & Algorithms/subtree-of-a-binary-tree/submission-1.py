# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val and self.treeEqual(root, subRoot):
            return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    def treeEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        return root.val == subRoot.val and self.treeEqual(root.right, subRoot.right) and self.treeEqual(root.left, subRoot.left)