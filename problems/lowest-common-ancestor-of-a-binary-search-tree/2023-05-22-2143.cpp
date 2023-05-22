// Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
// Accepted 2023-05-22 21:43 UTC · C++ · 41 ms · 23.3 MB

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        return ((root -> val > p -> val) && (root -> val > q -> val))
            ? lowestCommonAncestor(root -> left, p, q) 
            : ((root -> val < p -> val) && (root -> val < q -> val)) 
            ? lowestCommonAncestor(root -> right, p, q) 
            : root;
    }
};
