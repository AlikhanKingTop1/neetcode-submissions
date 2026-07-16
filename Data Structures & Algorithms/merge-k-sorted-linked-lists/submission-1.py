# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists:
                return None
            
            while len(lists) > 1:
                merge_lists = []
                lists_len = len(lists)
                for idx in range(0, lists_len, 2):
                    l1 = lists[idx]
                    new_idx = idx + 1
                    l2 = lists[new_idx] if new_idx < lists_len else None
                    new_list = self.merge_two_lists(l1,l2)
                    merge_lists.append(new_list)
                lists = merge_lists

            return lists[0]


    def merge_two_lists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2 
        return dummy.next