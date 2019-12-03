/***from dust i have come, dust i will be***/

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
    int ans = 0;
    void sum(TreeNode* root, int x)
    {
        if(root == NULL) return;
        
        x = x * 10 + root->val;
        if(root->left == NULL && root->right == NULL)
        {
            ans += x;
            return;
        }
        
        if(root->left)
            sum(root->left, x);
        if(root->right)
            sum(root->right, x);
    }
    int sumNumbers(TreeNode* root) {
        sum(root, 0);
        return ans;
    }
};
