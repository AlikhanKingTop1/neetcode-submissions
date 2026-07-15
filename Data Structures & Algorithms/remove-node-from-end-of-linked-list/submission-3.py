class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        i = 1
        while i <= n and right:
            i +=1
            right = right.next
        if not right:
            return head.next
        while right and right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head