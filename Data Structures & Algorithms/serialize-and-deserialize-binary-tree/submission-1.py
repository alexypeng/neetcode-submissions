# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        
        q = deque([root])
        res = []

        while q:
            node = q.popleft()

            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        if nodes[0] == "N":
            return None
        
        root = TreeNode(int(data[0]))
        q = deque([root])
        idx = 1

        while q:
            node = q.popleft()

            if nodes[idx] != "N":
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
        
            if nodes[idx] != "N":
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1

        return root


