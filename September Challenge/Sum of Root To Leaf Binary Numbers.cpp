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
#define pp pair<int, int>

class Solution {
public:
    int ans;
    vector<int> vec;
    
    void solve(TreeNode* root){
        // leaf
        if(root->left == NULL && root->right == NULL)
        {
            ans += root->val;  // leaf value, 2^0 * leaf
            int n = vec.size() - 1, p = 2;
            for(int i = n; i >= 0; i--)
                ans += vec[i] * p, p *= 2;
        }
        
        else {
            vec.push_back(root->val);
            
            if(root->left) solve(root->left);
            if(root->right) solve(root->right);
            
            vec.pop_back();
        }
    }
    
    int sumRootToLeaf(TreeNode* root) {
        this->ans = 0;
        solve(root);
        
        return this->ans;
    }
};
