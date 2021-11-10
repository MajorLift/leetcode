// Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/
// Accepted 2021-11-10 12:06 UTC · JavaScript · 76 ms · 38.4 MB

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    if (head === undefined || head === null) return null;
    let [curr, counter] = [head, 1];
    while (curr.next !== null) {
        curr = curr.next;
        counter += 1;
    }
    let mid = Math.floor(counter / 2) + 1;
    [curr, counter] = [head, 1];
    while (counter++ < mid) curr = curr.next;
    return curr;
};
