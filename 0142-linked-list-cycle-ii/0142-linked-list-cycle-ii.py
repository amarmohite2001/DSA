# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        pos = []
        while fast!= None and fast.next != None:
            fast = fast.next.next
            pos.append(slow)
            slow = slow.next
            if slow in pos:
                return slow
        return None
            
        