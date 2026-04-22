# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = node = ListNode()
        carry = 0

        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            
            val = v1 + v2 + carry

            carry = val // 10 
            val = val % 10

            node.next = ListNode(val)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        

        return curr.next

            
        