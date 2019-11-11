/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

typedef unsigned long long int ll;

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
    vector<pair<ll, ll>> vec;
    void solve(TreeNode* root, int level, ll num)
    {
        if(vec.size() < level + 1)
        {
            vec.push_back({num, num});
            //cout<<level<<" "<<num<<endl;
        }
        //cout<<level<<" x "<<num<<endl;
        
        vec[level].first = min(vec[level].first, num);
        vec[level].second = max(vec[level].second, num);
        
        if(root->left)
            solve(root->left, level + 1, 2 * num + 1);
        
        if(root->right)
            solve(root->right, level + 1, 2 * num + 2);
    }
    
    int widthOfBinaryTree(TreeNode* root) {
        vec.push_back({1, 1});
        
        if(root->left)
            solve(root->left, 1, 1);
        if(root->right)
            solve(root->right, 1, 2);
        
        ll ans = 1;
        int i, n = vec.size();
        
        for(i = 0; i < n; i++)
        {
            //cout<< vec[i].second << " " << vec[i].first << endl;
            if(vec[i].second == -1 || vec[i].first == 1e18) continue;
            ans = max(ans, vec[i].second - vec[i].first + 1);
        }
        
        return (int)ans;
    }
};
