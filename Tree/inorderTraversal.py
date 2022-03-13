# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        def dfs_trav(root):
            if root is None:
                return 
            dfs_trav(root.left)
            nums.append(root.val)
            dfs_trav(root.right)
            
        
        dfs_trav(root)
        return nums

# Iterative solution

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    stack , res = [] , []
    while True:
        
        while root is not None:
            stack.append(root)
            root = root.left
            
        if len(stack) == 0:
            break
        
        root = stack.pop()
        res.append(root.val)
        root = root.right
        
    return res
