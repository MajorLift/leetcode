// Count Good Nodes in Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/
// Accepted 2022-02-02 16:33 UTC · JavaScript · 281 ms · 78.1 MB

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function(root) {
    let output = 0;
    const stack = [[root, -Infinity]];
    while (stack.length) {
        const [curr, maxSoFar] = stack.pop();
        if (curr.val >= maxSoFar) output++;
        const newMaxSoFar = Math.max(curr.val, maxSoFar);
        if (curr.left) stack.push([curr.left, newMaxSoFar]);
        if (curr.right) stack.push([curr.right, newMaxSoFar]);
    }
    return output;
};
