# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        
        if not root:   #TreeNode is []
            return None
        
        stack=[root]  #store the TreeNode 
        while stack:
            #print("stack:",stack)
            node = stack.pop()  
            #print("pop stack:",stack)
            node.left, node.right  = node.right, node.left
            if node.left:
                #print("node left:")
                stack.append(node.left)
                #print("stack:",stack)
            if node.right:
                #print("node right:")
                stack.append(node.right)
                #print("stack:",stack)
        return root
