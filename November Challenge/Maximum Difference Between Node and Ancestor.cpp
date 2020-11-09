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
    void solve(TreeNode* root, pair<int, int> val) {
        if(!root) return;
        
        pair<int, int> m = val;
        m.first = min(val.first, root->val);
        m.second = max(val.second, root->val);
        
        if(root->left) solve(root->left, m);
        if(root->right) solve(root->right, m);
        
        // cout<<"in "<<root->val<<" "<<m.first<<" "<<m.second<<endl;
        if(!root->left && !root->right) ans = max(ans, m.second - m.first);
            
    }
    int maxAncestorDiff(TreeNode* root) {
        solve(root, {1e6, 0});
        return ans;
    }
};
