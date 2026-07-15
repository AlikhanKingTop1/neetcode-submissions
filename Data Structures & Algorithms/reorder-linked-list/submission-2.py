# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dq = deque()
        ptr = head
        while ptr:
            dq.append(ptr.val)
            ptr = ptr.next
        arr = []
        while dq:
            arr.append(dq.popleft())
            if dq:
                arr.append(dq.pop())
        curr = head
        for val in arr:
            curr.val = val
            curr = curr.next
        