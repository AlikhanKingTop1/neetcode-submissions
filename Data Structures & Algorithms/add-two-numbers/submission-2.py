# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Первый ЛЛ -> Массив
        cur = l1
        arr1 = []
        while cur:
            arr1.append(cur.val)
            cur = cur.next

        # Второй ЛЛ -> Массив
        cur = l2
        arr2 = []
        while cur:
            arr2.append(cur.val)
            cur = cur.next

        # Вручную развернул -> сделал числа нормальными
        arr1.reverse()
        arr2.reverse()

        # Из [1,2,3] -> 123
        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str, arr2))) 

        # Суммировал -> 123 + 456 = 579
        num3 = num1 + num2

        # Разворот суммы + засунуть числа в массив -> 579 -> 975 -> [9,7,5]

        rev = str(num3)[::-1]
        digits = list(map(int, str(rev)))

        # Обратно засунуть в ЛЛ, Массив -> ЛЛ
        dummy = ListNode(0)
        cur = dummy
        for val in digits:
            cur.next = ListNode(val)
            cur = cur.next

        # Вернуть ответ
        return dummy.next