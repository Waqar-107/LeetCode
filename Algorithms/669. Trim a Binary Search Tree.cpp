
class Solution {
public:
    //TreeNode* recur(TreeNode* )
    void solve(TreeNode* root, TreeNode* par, int L, int R, bool dir)
    {
        if(root == NULL) return;
        
        // cut the right part
        if(root->val > R)
        {
            if(dir)
                par->right = root->left;
            else
                par->left = root->left;
            
            solve(root->left, par, L, R, dir);
        }
        
        // cut the left part
        else if(root->val < L)
        {
            if(dir)
                par->right = root->right;
            else
                par->left = root->right;
            
            
            solve(root->right, par, L, R, dir);
        }
        
        else
        {
            if(root->right)
                solve(root->right, root, L, R, 1);
            
            if(root->left)
                solve(root->left, root, L, R, 0);
        }
    }
    
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        // find the actual root
        while(root)
        {
            if(root->val < L)
                root = root->right;
            else if(R < root->val)
                root = root->left;
            
            else break;
        }
        //cout<<root->val<<endl;
        if(root){
            solve(root->right, root, L, R, 1);
            solve(root->left, root, L, R, 0);
        }
        
        return root;
    }
};
