// Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/
// Accepted 2020-02-09 06:58 UTC · C · 4 ms · 7.7 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    if(head != NULL && head->next != NULL){
        struct ListNode* p = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return p;
    }
    return head;
}
