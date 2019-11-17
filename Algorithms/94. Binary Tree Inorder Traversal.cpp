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
    vector<int> vec;
public:
    void solve(TreeNode *root)
    {
        if(root == NULL) return;
        
        solve(root->left);
        vec.pb(root->val);
        solve(root->right);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        solve(root);
        return vec;
    }
};
