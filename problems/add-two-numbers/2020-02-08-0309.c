// Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/
// Accepted 2020-02-08 03:09 UTC · C · 16 ms · 9.1 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void push(struct ListNode* head, int val) {
    struct ListNode* current = head;
    while(current->next != NULL) {
        current = current->next;
    }
    current->next = (struct ListNode*) malloc(sizeof(struct ListNode));
    current->next->val = val;
    current->next->next = NULL;
    current = current->next;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    // init empty linked list for output
    struct ListNode* head = (struct ListNode*) malloc(sizeof(struct ListNode));
    head->next = NULL;
    // init pointers to parameters
    struct ListNode *p = l1, *q = l2, *current = head;
    
    int carry = 0;
    while(p != NULL || q != NULL) {
        int x = 0, y = 0;
        if(p != NULL) { x = p->val; }
        if(q != NULL) { y = q->val; }
        int sum = carry + x + y;        // 0 <= sum < 20
        carry = sum / 10;              // carry = 0 or 1
        push(current, sum % 10);
        if(p != NULL) { p = p->next; }
        if(q != NULL) { q = q->next; }
    }
    if (carry > 0) { push(current, carry); }
    return head->next;
}
