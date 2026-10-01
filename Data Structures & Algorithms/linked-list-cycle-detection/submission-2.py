# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        node = head

        while node:
            if node in seen:  #node.val is wrong  head=[1,2,1] index =-1
                return True
            else:
                seen.add(node)
            node = node.next
        
        return False
