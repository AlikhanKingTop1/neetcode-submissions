class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
        center = slow.next
        slow.next = None

        prev,cur = None, center
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        first,second = head, prev
        while first and second:
            first_tmp = first.next
            second_tmp = second.next
            first.next = second
            second.next = first_tmp
            first = first_tmp
            second = second_tmp
    