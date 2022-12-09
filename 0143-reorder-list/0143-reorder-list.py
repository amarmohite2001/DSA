# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #finding middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #reversing the second linkedlist
        second=slow.next
        prev=slow.next=None
        while second:
            after= second.next
            second.next=prev
            prev=second
            second=after
            
        #merge two halves
        first, second= head, prev
        while second:
            temp1, temp2= first.next, second.next
            first.next = second
            second.next=temp1
            first,second= temp1, temp2
        
            