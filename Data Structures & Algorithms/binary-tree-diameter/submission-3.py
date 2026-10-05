# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
            
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        dia = leftHeight + rightHeight
        subtree_dia = max(self.diameterOfBinaryTree(root.left),
                            self.diameterOfBinaryTree(root.right))
        res = max(dia,subtree_dia)
        
        return res

    def maxHeight(self,node):
        if not node:
            return 0

        height = 1+ max(self.maxHeight(node.left) ,self.maxHeight(node.right))
        return height