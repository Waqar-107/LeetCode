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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* x = root;
        if(root == NULL)
        {
            root = new TreeNode(val);
            return x;
        }
        
        while(true)
        {
            //cout<<root->val<<endl;
            if(root->val <= val)
            {
                if(root->right)
                    root = root->right;
                else
                {
                    root->right = new TreeNode(val);
                    break;
                }
            }
            
            else
            {
                if(root->left)
                    root = root->left;
                else
                {
                    root->left = new TreeNode(val);
                    break;
                }
            }
        }
        
        return x;
    }
};
