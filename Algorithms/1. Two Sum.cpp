/***from dust i have come, dust i will be***/

#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mp;
        vector<int> ans;
        
        for(int i = 0; i < nums.size(); i++)
            mp[nums[i]]++;

        for(int i = 0; i < nums.size(); i++)
        {
            if(target - nums[i] == nums[i] && mp[nums[i]] >= 2)
            {
                ans.push_back(i);
                for(int j = 0; j < nums.size(); j++)
                {
                    if(i != j && nums[j] == target - nums[i])
                    {
                        ans.push_back(j);
                        break;
                    }
                }

                break;
            }

            else if(target - nums[i] != nums[i] && mp[target - nums[i]])
            {
                ans.push_back(i);
                for(int j = 0; j < nums.size(); j++)
                {
                    if(nums[j] == target - nums[i])
                    {
                        ans.push_back(j);
                        break;
                    }
                }


                break;
            }
        }
        
        return ans;
    }
};
