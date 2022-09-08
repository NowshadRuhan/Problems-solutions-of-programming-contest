# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def hasSumHelper(root, curr_sum):
            if root == None: return False
            
            curr_sum += root.val
            if not root.left and not root.right and curr_sum == targetSum: 
                return True
            
            return hasSumHelper(root.left, curr_sum) or hasSumHelper(root.right, curr_sum)
            
        
        return hasSumHelper(root, 0)