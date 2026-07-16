# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first,second = l1,l2
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while first or second:
            x = first.val if first else 0
            y = second.val if second else 0
            digit = x + y + carry
            carry = 0
            carry = digit // 10
            digit %= 10
            cur.next = ListNode(digit)
            cur = cur.next
            first = first.next if first else None
            second = second.next if second else None
        if carry:
            cur.next = ListNode(1)
        return dummy.next