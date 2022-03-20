# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:           
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def builder(i , j):
            if i > j:
                return 
            mid = (i+j)//2
            node = TreeNode(nums[mid])
            node.left = builder(i , mid-1)
            node.right = builder(mid+1 , j)
            return node
        return builder(0 , len(nums)-1)
