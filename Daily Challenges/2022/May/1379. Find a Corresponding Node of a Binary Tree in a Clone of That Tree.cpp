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
    TreeNode* solve(TreeNode* root1, TreeNode* root2, TreeNode* target)
    {
        if(root1 == NULL) return NULL;
        
        if(root1->val == target->val)
            return root2;
        
        TreeNode* l = solve(root1->left, root2->left, target);
        TreeNode* r = solve(root2->right, root2->right, target);
        
        if(l != NULL) return l;
        return r;
    }
    
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        return solve(original, cloned, target);
    }
};
