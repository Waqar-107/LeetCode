/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int mn;
    void traverse(TreeNode* root, int cnt) {
        if(root == NULL) return;

        if(root->left == NULL && root->right == NULL) {
            mn = min(mn, cnt);
            return;
        }

        traverse(root->left, cnt + 1);
        traverse(root->right, cnt + 1);
    } 
    int minDepth(TreeNode* root) {
        if(root == NULL) return 0;
        
        mn = INT_MAX;
        traverse(root, 1);

        return mn;
    }
};
