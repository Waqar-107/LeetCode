/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> a;
        
        int i, j, m = nums2.size();
        for(i = m - 1; i >= 0; i--)
        {
            a[nums2[i]] = -1;
            for(j = i + 1; j < m; j++)
            {
                if(nums2[j] > nums2[i]){
                    a[nums2[i]] = nums2[j];
                    break;
                }
            }
        }
        
        m = nums1.size();
        vector<int> ans(m);
        for(i = 0; i < m; i++)
            ans[i] = a[nums1[i]];
        
        return ans;
    }
};
