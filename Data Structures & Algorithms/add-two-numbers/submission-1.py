# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        arr1 = []
        while cur:
            arr1.append(cur.val)
            cur = cur.next

        cur = l2
        arr2 = []
        while cur:
            arr2.append(cur.val)
            cur = cur.next
        
        arr1.reverse()
        arr2.reverse()

        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str, arr2)))

        num3 = num1 + num2
        print(num3)
        rev = str(num3)[::-1]
        print(rev)
        digits = list(map(int, str(rev)))
        print(digits)
        dummy = ListNode(0)
        cur = dummy
        for val in digits:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next