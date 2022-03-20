
class Solution:
    def solve(self , root , val):
        if root is not None:
            if root.val == val:
                return root
            
            return self.solve(root.left , val) or self.solve(root.right , val) 
                
                
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.solve(root , val)
