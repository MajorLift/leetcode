// Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/
// Accepted 2020-02-08 08:45 UTC · C · 0 ms · 7.2 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* swapPairs(struct ListNode* head){    
    struct ListNode* current = head;
    if(current != NULL && current->next != NULL){
        int tmp = current->val;
        current->val = current->next->val;
        current->next->val = tmp;
               
        current->next->next = swapPairs(current->next->next);
        return current;
    }
    else{
        return head;
    }
}
