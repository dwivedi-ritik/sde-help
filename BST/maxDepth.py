class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            if root is not None:
                m = max(1 +solve(root.left) , 1 + solve(root.right))
                return m
            return 0
        return solve(root)
        
