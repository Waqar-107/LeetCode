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
    int depth(TreeNode* root, int level)
    {
        if(root == NULL) return 0;
        
        if(root->left == NULL && root->right == NULL) return level;
        
        return max(depth(root->left, level + 1), depth(root->right, level + 1));
    }
    
    int getSumOfMaxDepth(TreeNode* root, int level, int maxDepth)
    {
        if(root == NULL) return 0;
        //cout << level << " " << root->val << " " << maxDepth << endl;
        if(level == maxDepth) return root->val;
        
        return getSumOfMaxDepth(root->left, level + 1, maxDepth) + getSumOfMaxDepth(root->right, level + 1, maxDepth);
    }
    
    int deepestLeavesSum(TreeNode* root) {
        int maxDepth = depth(root, 0);
        return getSumOfMaxDepth(root, 0, maxDepth);
    }
};
