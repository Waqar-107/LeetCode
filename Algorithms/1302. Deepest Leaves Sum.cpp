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
    int depth;
    void findDepth(TreeNode* root, int val){
        if(root == NULL) return;
        
        depth = max(depth, val);
        findDepth(root->left, val + 1);
        findDepth(root->right, val + 1);
    }
    
    int solve(TreeNode* root, int val){
        if(root == NULL) return 0;
        
        int cnt = 0;
        if(val == depth) cnt += root->val;
        
        cnt += solve(root->left, val + 1);
        cnt += solve(root->right, val + 1);
        
        return cnt;
    }
    
    int deepestLeavesSum(TreeNode* root) {
        depth = 0;
        findDepth(root, 0);
        
        return solve(root, 0);
    }
};
