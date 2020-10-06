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
    TreeNode* solve(TreeNode* root, TreeNode* parent, int val, int ch)
    {
        if(root == NULL) {
            root = new TreeNode(val);
            if(parent) {
                if(!ch) parent->left = root;
                else parent->right = root;
            }
            
            return root;
        }
        
        if(val > root->val)
            solve(root->right, root, val, 1);
        
        else
            solve(root->left, root, val, 0);
        
        return root;
    }
    
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        return solve(root, NULL, val, -1);
    }
};
