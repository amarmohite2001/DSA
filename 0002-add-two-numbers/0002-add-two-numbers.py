# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0
        while (l1!=None or l2!=None or carry!=0):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val +carry
            #modulus operator(taking the reminder if there is any) 12%10 = 2
            head.next = ListNode(total%10)
            #floor division- takes e.g= 12//10 = 1
            carry = total//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            head= head.next
        return dummy.next
        