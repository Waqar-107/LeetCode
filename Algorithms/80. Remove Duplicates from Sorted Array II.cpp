/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i, j, k = 0, cnt = 0;
        int n = nums.size();
        
        i = 0;
        while(i < n)
        {
            cnt = 1;
            cout<<i<<" "<<nums[i]<<endl;
            nums[k] = nums[i]; k++;
            for(j = i + 1; j < n; j++)
            {
                if(nums[i] == nums[j])
                {
                    if(cnt == 1)
                        nums[k] = nums[i], k++, cnt++;
                }
                
                else break;
            }
            
            i = j;
        }
        
        while(nums.size() > k) nums.pop_back();
        return nums.size();
    }
};
