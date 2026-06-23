/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* next = nullptr;

        while (head != nullptr) {
            next = head->next;    // сохраняем указатель на следующий узел
            head->next = prev;    // переворачиваем указатель на предыдущий узел
            prev = head;          // перемещаем prev на текущий узел
            head = next;          // переходим к следующему узлу
        }
        head = prev;  // теперь prev указывает на новый первый элемент
    }
};
