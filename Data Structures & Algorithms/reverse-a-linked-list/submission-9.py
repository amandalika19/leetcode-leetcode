# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #TLDR: have a next pointer that can continue along while i revert curr.next the opposite direction, keeping prev and next ptr as the boundaries 
        curr = head
        prev = None

        while curr:

            nextPtr = curr.next
            curr.next = prev
            prev = curr
            curr = nextPtr
        
        return prev
