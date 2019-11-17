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
    vector<vector<int>> vec;
public:
    void solve(TreeNode* root, int idx){
        if(root == NULL) return;
        
        if(vec.size() < idx)
        {
            vector<int> v(1, root->val);
            vec.pb(v);
        }
        
        else
            vec[idx - 1].pb(root->val);
        
        solve(root->left, idx + 1);
        solve(root->right, idx + 1);
    }
    
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        solve(root, 1);
        for(int i = 0; i < vec.size(); i++)
        {
            if(i % 2)
                reverse(vec[i].begin(), vec[i].end());
        }
        
        return vec;
    }
};
