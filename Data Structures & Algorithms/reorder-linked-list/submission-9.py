# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        #find the middle 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = slow.next = None

        #reverse the second half
        while curr:
            nextptr = curr.next
            curr.next = prev
            prev = curr
            curr = nextptr
    
        #adjacent nodes
        f, s = head, prev
        while s:
            t1, t2 = f.next, s.next
            f.next = s
            s.next = t1
            f, s = t1, t2