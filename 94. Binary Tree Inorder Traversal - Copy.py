# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        result = []
        def travel(root):
            if root is None:
                return
            travel(root.left)
            result.append(root.val)
            travel(root.right)
            
            return
       
        travel(root) 
        return result