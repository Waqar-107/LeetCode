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
    int ans = 0;
    
    int solve(TreeNode* root) {
        int L = 0, R = 0;
        
        if(root->left)
            L = solve(root->left);
        if(root->right)
            R = solve(root->right);
        
        ans += abs(L - R);
        return (L + R + root->val);
    }
    
    int findTilt(TreeNode* root) {
        if(root == NULL) return 0;
        solve(root);
        
        return ans;
    }
};
