# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow)    
        prev = None
        while slow:
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        # print(prev)
        total = 0
        left, right = head, prev
        while right:
            add = left.val + right.val
            if add>=total:
                total = add
            left = left.next
            right= right.next
        return total
            
            
            
        