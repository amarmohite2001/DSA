# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(200,next=head)
        prev = dummy
        while head:
            if prev.val == head.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
        