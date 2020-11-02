class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        set<int> distinct_candies;
        for(int e : candies)
            distinct_candies.insert(e);
        
        return min(candies.size() / 2, distinct_candies.size());
    }
};
