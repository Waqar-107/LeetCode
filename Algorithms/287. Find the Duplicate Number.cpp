/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int tortoise = nums[0], hare = nums[0];
        while(true){
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
            
            if(hare == tortoise) break;
        }
        
        tortoise = nums[0];
        while(tortoise != hare){
            tortoise = nums[tortoise];
            hare = nums[hare];
        }
        
        return tortoise;
    }
};
