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
    int rangeSumBST(TreeNode* root, int L, int R) {
        if(root == NULL) return 0;
        
        int ret = 0;
        if(root->val >= L && root->val <= R)
            ret += root->val;
        
        ret += rangeSumBST(root->left, L, R);
        ret += rangeSumBST(root->right, L, R);
        
        return ret;
    }
};
