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
                
            nums.append(root.val)
            dfs_trav(root.left)
            dfs_trav(root.right)
            
        
        dfs_trav(root)
        return nums
