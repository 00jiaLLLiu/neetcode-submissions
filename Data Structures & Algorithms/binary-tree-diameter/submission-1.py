# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res=0

        def dfs(curr): #bottom to top of the tree
            if not curr:
                return 0

            left = dfs(curr.left) 
            right = dfs(curr.right)
            self.res =max(self.res,left+right)

            return 1+ max(left,right) # 孩子->自己的最长边 + 自己->parent 的1条

        dfs(root)
        return self.res

