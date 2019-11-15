/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

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
    TreeNode* ans;
    int solve(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        if(root == NULL) return 0;
        
        int cnt = 0;
        if(root == p) cnt++;
        if(root == q) cnt++;
        
        cnt += solve(root->left, p, q);
        cnt += solve(root->right, p, q);
        
        if(cnt == 2 && ans == NULL)
            ans = root;
        //cout<<root->val<<" "<<cnt;nl;
        return cnt;
    }
    
    
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        ans = NULL;
        solve(root, p, q);
        return ans;
    }
};
